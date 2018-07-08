// we load the initial image inline, the restof them are loaded async

var img_ids = ["img2", "img3", "img4", "img5", "img6", "img7", "img8", "img9", "img10", "img11", "img12", "img13", "img14", "img15", "img16", "img17", "img18", "img19", "img20", "img21", "img22", "img23", "img24", "img25", "img26", "img27", "img28", "img29", "img30", "img31", "img32", "img33", "img34", "img35", "img36", "img37", "img38", "img39", "img40", "img41", "img42", "img43", "img44", "img45", "img46", "img47", "img48", "img49", "img50", "img51", "img52", "img53", "img54", "img55", "img56", "img57", "img58", "img59", "img60", "img61", "img62", "img63", "img64", "img65", "img66", "img67", "img68", "img69", "img70", "img71", "img72", "img73", "img74", "img75", "img76", "img77", "img78", "img79", "img80", "img81", "img82", "img83", "img84", "img85", "img86", "img87", "img88", "img89", "img90", "img91", "img92", "img93", "img94", "img95", "img96", "img97", "img98", "img99", "img100", "img101", "img102", "img103"];

var lang_codes = ["am", "ar", "az", "be", "bg", "bn", "bs", "ca", "ceb", "co", "cs", "cy", "da", "de", "el", "eo", "es", "et", "eu", "fa", "fi", "fr", "fy", "ga", "gd", "gl", "gu", "ha", "haw", "hi", "hmn", "hr", "ht", "hu", "hy", "id", "ig", "is", "it", "iw", "ja", "jw", "ka", "kk", "km", "kn", "ko", "ku", "ky", "la", "lb", "lo", "lt", "lv", "mg", "mi", "mk", "ml", "mn", "mr", "ms", "mt", "my", "ne", "nl", "no", "ny", "pa", "pl", "ps", "pt", "ro", "ru", "sd", "si", "sk", "sl", "sm", "sn", "so", "sq", "sr", "st", "su", "sv", "sw", "ta", "te", "tg", "th", "tl", "tr", "uk", "ur", "uz", "vi", "xh", "yi", "yo", "zh-CN", "zh-TW","zu"];

for(var i=0;i<img_ids.length;i++) {
	var downloadingImage = new Image();
	downloadingImage.onload = function(){
		document.getElementById(img_ids[i]).src = downloadingImage.src;
		console.log("inside");
		console.log(document.getElementById(img_ids[i]).id);
		console.log(document.getElementById(img_ids[i]).src);
	};
	console.log("outside");
	console.log(img_ids[i]);
	downloadingImage.src = "https:/devangthakkar.github.io/assets/chain_images/chain_".concat(lang_codes[i].concat(".svg"));
}