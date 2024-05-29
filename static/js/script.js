
document.addEventListener('DOMContentLoaded', function() {
  const data = {
    labels: [
      'Red',
      'Blue',
      'Yellow'
    ],
    datasets: [{
      label: 'My First Dataset',
      data: [300, 50, 100],
      backgroundColor: [
        'rgb(255, 99, 132)',
        'rgb(255,140,0)',
        'rgb(75, 192, 192)'
      ],
      hoverOffset: 4
    }]
  };
  var options = {
    responsive: true
  };
  var ctx = document.getElementById('myChart').getContext('2d');
  var myChart = new Chart(ctx, {
    type: 'pie',
    data: data,
    options: options
  });
});

document.addEventListener('DOMContentLoaded', function() {
  const data = {
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'July', 'July', 'July', 'July'],
    datasets: [{
      label: 'My Dataset',
      data: [65, 59, 80, 81, 56, 55, 40, 40, 40, 50, 60],
      fill: false,
      borderColor: 'rgb(75, 192, 192)',
      tension: 0.1
    }]
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      y: {
        display: true,
      }
    }
  };

  const ctx = document.getElementById('myline').getContext('2d');
  const myline = new Chart(ctx, {
    type: 'line',
    data: data,
    options: options
  });
});

document.addEventListener('DOMContentLoaded', function() {
  const radarData = {
    labels: ['Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5', 'Label 6'],
    datasets: [{
      label: 'Radar Dataset',
      data: [10, 20, 30, 40, 50, 60],
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
      borderColor: 'rgba(255, 99, 132, 1)',
      borderWidth: 1
    },
    {
      label: 'Radar Dataset',
      data: [20, 10, 60, 30,60, 40],
      backgroundColor: 'rgb(75, 192, 192, 0.2)',
      borderColor: 'rgb(75, 192, 192)',
      borderWidth: 1
    }]
  };

  const radarOptions = {
    responsive: true,
    maintainAspectRatio: false,
    scale: {
      ticks: {
        beginAtZero: true
      }
    }
  };

  const radarCtx = document.getElementById('myRadarChart').getContext('2d');
  const myRadarChart = new Chart(radarCtx, {
    type: 'radar',
    data: radarData,
    options: radarOptions
  });
});

/*===== EXPANDER MENU  =====*/ 
const showMenu = (toggleId, navbarId, bodyId)=>{
  const toggle = document.getElementById(toggleId),
  navbar = document.getElementById(navbarId),
  bodypadding = document.getElementById(bodyId)

  if(toggle && navbar){
    toggle.addEventListener('click', ()=>{
      navbar.classList.toggle('expander')

      bodypadding.classList.toggle('body-pd')
    })
  }
}
showMenu('nav-toggle','navbar','body-pd')

/*===== LINK ACTIVE  =====*/ 
const linkColor = document.querySelectorAll('.nav__link')
function colorLink(){
  linkColor.forEach(l=> l.classList.remove('active'))
  this.classList.add('active')
}
linkColor.forEach(l=> l.addEventListener('click', colorLink))


/*===== COLLAPSE MENU  =====*/ 
const linkCollapse = document.getElementsByClassName('collapse__link')
var i

for(i=0;i<linkCollapse.length;i++){
  linkCollapse[i].addEventListener('click', function(){
    const collapseMenu = this.nextElementSibling
    collapseMenu.classList.toggle('showCollapse')

    const rotate = collapseMenu.previousElementSibling
    rotate.classList.toggle('rotate')
  })
}

