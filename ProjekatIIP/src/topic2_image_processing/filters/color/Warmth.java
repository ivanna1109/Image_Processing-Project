package topic2_image_processing.filters.color;

import javafx.scene.paint.Color;
import topic2_image_processing.filters.ColorFilter;

public class Warmth extends ColorFilter{

	private int i;
	private int j;
	
	public Warmth(int i, int j) {
		this.i = i;
		this.j = j;
	}

	@Override
	public Color processColor(Color input) {
		double newRed = input.getRed() + i/255.0;
		if(newRed > 1.0) newRed = 1.0;
		
		double newBlue = input.getBlue() - j/255.0;
		if(newBlue < 0.0) newBlue = 0.0;
		
		return new Color(newRed, input.getGreen(), newBlue, input.getOpacity());
	}

}
