document.addEventListener('DOMContentLoaded', function () {
  var menuToggle = document.getElementById('menu-toggle');
  var menuPopover = document.getElementById('menu-popover');

  function openMenu() {
    menuPopover.style.display = 'block';
  }

  function closeMenu() {
    menuPopover.style.display = 'none';
  }

  // Toggle menu on button click
  menuToggle.addEventListener('click', function (e) {
    e.stopPropagation();
    if (menuPopover.style.display === 'block') {
      closeMenu();
    } else {
      openMenu();
    }
  });

  // Prevent clicks inside the popover from closing it
  menuPopover.addEventListener('click', function (e) {
    e.stopPropagation();
  });

  // Close menu when clicking outside
  document.addEventListener('click', function () {
    closeMenu();
  });

  // Close menu on ESC key
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      closeMenu();
    }
  });

  // Hide menu by default
  closeMenu();
});
