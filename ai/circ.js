function polarToCartesian(centerX, centerY, radius, angleInDegrees) {
	var angleInRadians = (angleInDegrees-90) * Math.PI / 180.0;

	return {
		x: centerX + (radius * Math.cos(angleInRadians)),
		y: centerY + (radius * Math.sin(angleInRadians))
	};
}

function describeArc(x, y, radius, startAngle, endAngle){

		var start = polarToCartesian(x, y, radius, endAngle);
		var end = polarToCartesian(x, y, radius, startAngle);

		var largeArcFlag = endAngle - startAngle <= 180 ? "0" : "1";

		var d = [
				"M", start.x, start.y, 
				"A", radius, radius, 0, largeArcFlag, 0, end.x, end.y
		].join(" ");

		return d;       
}

for (var i = 1; i <= 100; i++) {
	console.log(describeArc(350, 350, 200+i, (i-1)*3.6, i*3.6));
};