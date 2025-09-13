document.addEventListener('DOMContentLoaded', function () {
  const lists = document.querySelectorAll('.paginated-list');
  lists.forEach(list => {
    const pageSize = parseInt(list.getAttribute('data-page-size') || '12', 10);

    // Determine what to paginate:
    // 1) Per-year sections on Data Viz
    // 2) Otherwise, normalize by finding archive items and hiding their grid wrapper if present
    let items = Array.from(list.querySelectorAll('.year-section'));
    if (items.length === 0) {
      const raw = Array.from(list.querySelectorAll('.archive__item'));
      const mapped = raw.map(el => el.closest('.grid__item') || el);
      // de-duplicate while preserving order
      const seen = new Set();
      items = mapped.filter(el => {
        if (seen.has(el)) return false;
        seen.add(el);
        return true;
      });
    }

    if (items.length <= pageSize) return; // nothing to do

    let visible = pageSize;
    const apply = () => {
      items.forEach((el, i) => {
        el.style.display = (i < visible) ? '' : 'none';
      });
      if (visible >= items.length) {
        btn.style.display = 'none';
      } else {
        btn.style.display = '';
      }
    };

    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'btn btn--primary load-more';
    btn.textContent = 'Load more';
    btn.addEventListener('click', () => {
      visible = Math.min(visible + pageSize, items.length);
      apply();
      btn.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });

    // Insert button after the grid wrapper if present to avoid landing inside the grid
    const container = (list.parentElement && list.parentElement.classList && list.parentElement.classList.contains('grid__wrapper'))
      ? list.parentElement
      : list;
    container.insertAdjacentElement('afterend', btn);
    apply();
  });
});
