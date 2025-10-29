(function () {
  var $ = django.jQuery;
  $(document).ready(function () {
    $('textarea.markdown-editor').each(function (idx, el) {
      CodeMirror.fromTextArea(el, {
        lineNumbers: true,
        lineWrapping: true,
        mode: 'markdown',
        theme: 'monokai',
      });
    });
  });
})();
