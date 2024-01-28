package topic2_image_processing.filters.color;

import javafx.scene.paint.Color;
import topic2_image_processing.filters.ColorFilter;

/**
 * Cini boje na slici zasicenijim u zavisnosti od parametra zadatog u konstruktoru.
 */
public class Saturate extends ColorFilter {
	final double k;
	
	
	public Saturate(double k) {
		if(k > 1.0) k = 1.0;
		if(k < -1.0) k = -1.0;
		this.k = k;
	}


	@Override
	public Color processColor(Color input) {
		double s = input.getSaturation();
		
		if(k >= 0.0 && k <= 1.0)
			return Color.hsb(
					input.getHue(),
					s + k * (1 - s),          // Linearna interpolacija. Kada k ide od 0 do 1, ovaj izraz ide od s do 1.
					input.getBrightness(),
					input.getOpacity()
					);
		else
			return Color.hsb(
					input.getHue(),
					s * (1 - Math.abs(k)),          
					input.getBrightness(),
					input.getOpacity()
					);
	}
	
}	
