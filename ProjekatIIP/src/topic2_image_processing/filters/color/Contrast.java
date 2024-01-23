package topic2_image_processing.filters.color;

import javafx.scene.paint.Color;
import topic2_image_processing.filters.ColorFilter;

public class Contrast extends ColorFilter{

	private double factor;

	public Contrast(double factor) {
		this.factor = factor;
	}
	
	@Override
	public Color processColor(Color input) {
		double newR = 0.5 + factor * (input.getRed() - 0.5);
		double newG = 0.5 + factor * (input.getGreen() - 0.5);
		double newB = 0.5 + factor * (input.getBlue() - 0.5);
		
		if(newR > 1.0) newR = 1.0;
		if(newR < 0.0) newR = 0.0;
		
		if(newG > 1.0) newG = 1.0;
		if(newG < 0.0) newG = 0.0;
		
		if(newB > 1.0) newB = 1.0;
		if(newB < 0.0) newB = 0.0;
		
		Color newC = new Color(newR, newG, newB, input.getOpacity());
		return newC;
	}

}
