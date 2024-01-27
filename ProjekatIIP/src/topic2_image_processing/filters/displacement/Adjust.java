package topic2_image_processing.filters.displacement;

import mars.geometry.Vector;
import topic2_image_processing.filters.DisplacementFilter;
import topic2_image_processing.filters.Filter;


public class Adjust extends DisplacementFilter {
	
	private double alpha;
	
	public Adjust(double alpha) {
		this.alpha = alpha;
	}


	@Override
	public Vector source(Vector dst, Vector dim) {
		Vector mid = dim.div(2);
		if(alpha < -25) alpha = -25;
		if(alpha > 25) alpha = 25;
		double alphaRadians = Math.toRadians(alpha);
		double rotateCos = Math.cos(alphaRadians);
		double rotateSin = Math.sin(alphaRadians);
		double x1 = rotateCos * (dst.x - mid.x) - rotateSin * (dst.y - mid.y) + mid.x;
		double y1 = rotateSin * (dst.x - mid.x) + rotateCos * (dst.y - mid.y) + mid.y;
		if(x1 < 0 || x1 > dim.x || y1 < 0 || y1 > dim.y) {
			x1 = 0;
			y1 = 0;
		}
		return new Vector(x1, y1);
	}
	
}
