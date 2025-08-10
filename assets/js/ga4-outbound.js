document.addEventListener('click', function(e) {
    const a = e.target.closest('a[href]');
    if (!a) return;
    const href = a.getAttribute('href');
    const external = href.startsWith('http') && !href.includes(location.host);
    if (external && window.gtag) {
      gtag('event', 'click', {
        event_category: 'outbound',
        event_label: href,
        transport_type: 'beacon'
      });
    }
  }, { capture: true });