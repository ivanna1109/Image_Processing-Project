package topic2_image_processing.filters.color;

import javafx.scene.paint.Color;
import topic2_image_processing.filters.ColorFilter;

public class Shadows extends ColorFilter{
	
	private double coef;
	private double shadowTresh;

	public Shadows(double coef, double shadowTresh) {
		this.coef = coef;
		this.shadowTresh = shadowTresh;
	}
	
	@Override
	public Color processColor(Color input) {
		double intensity = (input.getRed() + input.getGreen() + input.getBlue()) / 3;
		double r = input.getRed();
		double g = input.getGreen();
		double b = input.getBlue();
		
		if(intensity < shadowTresh) {
			r *= coef;
			g *= coef;
			b *= coef;
			
			if(r > 1.0) r = 1.0;
			if(g > 1.0) g = 1.0;
			if(b > 1.0) b = 1.0;
			
			if(r < 0.0) r = 0.0;
			if(g < 0.0) g = 0.0;
			if(b < 0.0) b = 0.0;
		}
		return new Color(r, g, b, input.getOpacity());
	}

}
