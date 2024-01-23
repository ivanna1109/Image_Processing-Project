package topic2_image_processing.filters.color;

import javafx.scene.paint.Color;
import topic2_image_processing.filters.ColorFilter;

public class Fade extends ColorFilter {

	private double coef;

	public Fade(double coef) {
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
