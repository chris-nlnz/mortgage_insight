$(document).ready(function() {
    $('body').addClass('loaded');
});
window.onbeforeunload = function () {
    $('body').removeClass('loaded');
};
