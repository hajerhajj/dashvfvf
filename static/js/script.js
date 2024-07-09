
/*===== LINK ACTIVE  =====*/ 
const linkColor = document.querySelectorAll('.nav__link')
function colorLink(){
  linkColor.forEach(l=> l.classList.remove('active'))
  this.classList.add('active')
}
linkColor.forEach(l=> l.addEventListener('click', colorLink))


/*===== COLLAPSE MENU  =====*/ 
document.addEventListener('DOMContentLoaded', function() {
  const linkCollapse = document.querySelectorAll('.collapse__link');

  linkCollapse.forEach(function(collapseLink) {
      collapseLink.addEventListener('click', function() {
          const collapseMenu = this.nextElementSibling;
          collapseMenu.classList.toggle('showCollapse');

          const rotateIcon = this.querySelector('.collapse__icon');
          rotateIcon.classList.toggle('rotate');
      });
  });
});

 // Button and Table Show/Hide
  $('#mmeBtn').click(function(e) {
    e.preventDefault();
    $('.mme-section').hide();
    $('#mmeContainer').show();
  });

  $('#intBtn').click(function(e) {
    e.preventDefault();
    const intVisible = $('#intContainer').is(':visible');
    if (!intVisible) {
      $('.mme-section').hide();
      $('#intContainer').show();
    }
  });

  $('#globalBtn').click(function(e) {
    e.preventDefault();
    const globalVisible = $('#globalContainer').is(':visible');
    if (!globalVisible) {
      $('.mme-section').hide();
      $('#globalContainer').show();
    }
  });

  $('.nav__link').not('#mmeBtn, #intBtn').click(function() {
    $('.mme-section').hide();
  });

  // Flatpickr
  flatpickr("#dateRangePicker", {
    mode: "range",
    dateFormat: "Y-m-d"
  });

  // Custom Button Active
  $('.custom-button').click(function() {
    $('.custom-button').removeClass('active');
    $(this).addClass('active');
  });

  // Go Button Click
  $('#goBtn').click(function(e) {
    e.preventDefault();
    const selectedOption = $('.custom-select').val();
    $('.table-section').hide();
    $('#' + selectedOption.toLowerCase() + '_table').show();
  });



  