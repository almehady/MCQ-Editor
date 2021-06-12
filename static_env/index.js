tinymce.init({
    selector: 'textarea.ascii-tinymce',
    external_plugins: {'mathSymbols': '/static/plugin.js'},
    plugins: [
        'advlist autolink lists link image charmap print preview anchor',
        'searchreplace visualblocks code fullscreen',
        'insertdatetime media table paste code help wordcount mathSymbols',
    ],
    toolbar: 'mathjax | undo redo | formatselect | bold italic backcolor | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | removeformat | help | mathSymbols'
});