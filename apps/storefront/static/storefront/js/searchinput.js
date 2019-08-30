// updated 2019
// const input = document.getElementById("search-input");
// const searchBtn = document.getElementById("search-btn");

// const expand = () => {
//   searchBtn.classList.toggle("close");
//   input.classList.toggle("square");
// };

// searchBtn.addEventListener("click", expand);




//  old version / jquery
$(document).ready(function() {
	function expand() {
	  $(".search").toggleClass("close");
	  $(".input").toggleClass("square");
	  if ($('.search').hasClass('close')) {
	    $('#search-input').focus();
	  } else {
	    $('#search-input').blur();
	  }
	}
	$('#search-btn').on('click', expand);

})

