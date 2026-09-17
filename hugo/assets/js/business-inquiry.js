/* An inquiry is classified for Glezper's review; it is never sent to a partner. */
(function () {
  const form = document.getElementById('glezper-inquiry');
  if (!form) return;
  const interests = [...form.querySelectorAll('[data-service]')];
  const sections = [...form.querySelectorAll('[data-section]')];
  const selectedServices = () => interests.filter(input => input.checked).map(input => input.dataset.service);

  function syncFields() {
    const selected = selectedServices();
    interests[0].setCustomValidity(selected.length ? '' : form.dataset.serviceError);
    for (const section of sections) {
      const active = selected.includes(section.dataset.section);
      section.hidden = !active;
      section.disabled = !active;
      for (const input of section.querySelectorAll('input, select, textarea')) {
        const wrapper = input.closest('[data-when-field]');
        const matches = !wrapper || wrapper.dataset.whenValues.split(',').includes(form.elements.namedItem(wrapper.dataset.whenField).value);
        if (wrapper) wrapper.hidden = !matches;
        input.disabled = !active || !matches;
        input.required = active && matches && input.dataset.required === 'true';
      }
    }
    const opfRoute = document.getElementById('opf-qualified-route');
    const established = ['3_to_5_months', '6_to_11_months', '1_to_2_years', 'over_2_years'].includes(form.elements.namedItem('business_stage').value);
    if (opfRoute) opfRoute.hidden = revenueSegment() !== 'monthly_10000_or_more' || !established;
  }

  function revenueSegment() {
    if (!selectedServices().includes('financing')) return 'not_requested';
    const revenue = form.elements.namedItem('monthly_revenue').value;
    if (['10000_24999', '25000_49999', '50000_plus'].includes(revenue)) return 'monthly_10000_or_more';
    if (['pre_revenue', 'under_5000', '5000_9999'].includes(revenue)) return 'monthly_under_10000';
    return 'manual_review';
  }

  const button = form.querySelector('button[type="submit"]');
  const buttonLabel = button.querySelector('[data-submit-label]');
  const originalLabel = buttonLabel.textContent;
  form.addEventListener('change', syncFields);
  form.addEventListener('submit', function (event) {
    if (form.dataset.deliveryEnabled !== 'true') { event.preventDefault(); return; }
    syncFields();
    if (!form.reportValidity()) { event.preventDefault(); return; }
    const selected = selectedServices();
    const segment = revenueSegment();
    form.elements.namedItem('revenue_segment').value = segment;
    form.elements.namedItem('_subject').value = 'Glezper Business | ' + selected.join(' + ') + ' | ' + segment;
    // Include readable labels as well as stable field codes in the email.
    const summary = [];
    for (const input of form.querySelectorAll('input, select, textarea')) {
      if (input.disabled || input.type === 'hidden' || input.name === '_honey' || !input.value) continue;
      if (input.type === 'checkbox' && !input.checked) continue;
      const label = input.labels?.[0]?.textContent.trim() || input.name;
      const value = input.tagName === 'SELECT' ? input.selectedOptions[0].textContent.trim() : input.value;
      summary.push(label + ': ' + value);
    }
    form.elements.namedItem('inquiry_summary').value = summary.join('\n');
    // Keep native POST and the provider's default CAPTCHA. The provider handles
    // acceptance and redirect; no client-side "success" or automatic referral.
    button.disabled = true;
    buttonLabel.textContent = form.dataset.sending;
  });
  window.addEventListener('pageshow', function () {
    button.disabled = form.dataset.deliveryEnabled !== 'true';
    buttonLabel.textContent = originalLabel;
    syncFields();
  });
  syncFields();
})();
