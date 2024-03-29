package topic2_image_processing.filters.displacement;

import mars.geometry.Vector;
import topic2_image_processing.filters.DisplacementFilter;


/**
 * Uvelicava gornji levi cosak slike koristeci zadati zoom faktor.
 */
public class Zoom extends DisplacementFilter {
	final double k;
	
	
	public Zoom(double k) {
		if(k < 1) k = 1;
		if(k > 10) k = 10;
		this.k = k;
	}
	
	
	@Override
	public Vector source(Vector dst, Vector dim) {
		// Delimo obe koordinate vektora sa k.
		Vector center = dim.div(2);
		Vector translation = dst.sub(center);
		Vector scaled = translation.div(k);
		return scaled.add(center);
	}
	
}
