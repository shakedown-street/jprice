(function () {
  var html = document.documentElement;
  var themeToggle = document.getElementById('theme-toggle');
  var character = {
    light: '&#9790', // moon
    dark: '&#9728', // sun
  };

  var savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
    html.setAttribute('data-theme', savedTheme);
    themeToggle.innerHTML = character[savedTheme === 'dark' ? 'dark' : 'light'];
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      var currentTheme = html.getAttribute('data-theme');
      var newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', newTheme);
      themeToggle.innerHTML = character[newTheme === 'dark' ? 'dark' : 'light'];
      localStorage.setItem('theme', newTheme);
    });
  }
})();
