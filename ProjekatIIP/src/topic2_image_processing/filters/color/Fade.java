package topic2_image_processing.filters.color;

import javafx.scene.paint.Color;
import topic2_image_processing.filters.ColorFilter;

public class Fade extends ColorFilter {

	private double coef;

	public Fade(double coef) {
		if(coef > 1.0) coef = 1.0;
		if(coef < 0.0) coef = 0.0;
		this.coef = coef;
	}
	
	@Override
	public Color processColor(Color input) {
		double r = input.getRed();
		double g = input.getGreen();
		double b = input.getBlue();
		double o = (1 - coef) * input.getOpacity();
		
		return new Color(r, g, b, o);
	}

}
