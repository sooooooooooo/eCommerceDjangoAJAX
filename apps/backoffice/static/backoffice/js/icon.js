$(document).ready(function() {

	$.fn.selectpicker.Constructor.BootstrapVersion = '4';
	$("select").selectpicker();

	// targ=document.getElementsByClassName('dropdown-toggle')[0]
	targ1=$("#nSelect button")[0]
	targ2=$("#eSelect button")[0]
		
		newfun = function(){
				
				$("div.dropdown-menu li").hover(function() {
			// console.log($(this)[0].children[0].children[0])
			var spot = $(this)[0].children[0].children
			// $(this)[0].children[0].children[0].append("<i class='material-icons'>delete_forever</i>")
			$("<a href='https://www.google.com/' style='color:black;' class='myIcons'><i class='material-icons float-right'>delete_forever</i></a><a href='#' style='color:black;' class='myIcons'><i class='material-icons float-right'>edit</i></a>").insertAfter($(this)[0].children[0])
		}, function() {
			$("a.myIcons").remove()
		})

		}
		
		
		// targ.addEventListener("click", function(){newfun()}, {once: true});
		targ1.addEventListener("click", function(){newfun()}, {once: true});
		targ2.addEventListener("click", function(){newfun()}, {once: true});
		// targ.addEventListener("click", function(){console.log('chris is awesome')});
		// targ1.addEventListener("click", function(){console.log('chris is awesome 1')});
		// targ2.addEventListener("click", function(){console.log('chris is awesome 2')});

	
		
	// 	newfun = function(){
				
	// 			$("div.dropdown-menu li").hover(function() {
	// 		// console.log($(this)[0].children[0].children[0])
	// 		var spot = $(this)[0].children[0].children
	// 		// $(this)[0].children[0].children[0].append("<i class='material-icons'>delete_forever</i>")
	// 		$("<a href='#' style='color:black;'><i class='material-icons float-right'>delete_forever</i></a><a href='#' style='color:black;'><i class='material-icons float-right'>edit</i></a>").insertAfter($(this)[0].children[0].children[0])
	// 	}, function() {
	// 		$("i").remove()
	// 	})

	// 	}
		
		
	// 	targ1.addEventListener("click", function(){newfun()});
	// 	targ1.addEventListener("click", function(){console.log('chris is awesome')});


});