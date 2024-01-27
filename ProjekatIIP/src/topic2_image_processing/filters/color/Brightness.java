package topic2_image_processing.filters.color;

import javafx.scene.paint.Color;
import mars.drawingx.gadgets.annotations.GadgetDouble;
import topic2_image_processing.filters.ColorFilter;

public class Brightness extends ColorFilter {
	
	double brightnessFactor;
	
	public Brightness(double bf) {
		if(bf > 1.0) bf = 1.0;
		if(bf < 0.0) bf = 0.0;
		this.brightnessFactor = bf;
	}
	
	@Override
	public Color processColor(Color input) {
		double b = input.getBrightness();
		return Color.hsb(input.getHue(), 
						 input.getSaturation(),
						 b + (1 - b) * brightnessFactor);
	}

}
