document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('a[href^="http"]').forEach(a => {
      if (!a.href.includes(location.host)) {
        a.setAttribute('target','_blank');
        a.setAttribute('rel','noopener');
      }
    });
  });