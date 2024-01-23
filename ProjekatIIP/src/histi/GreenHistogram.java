package histi;

import javafx.scene.image.Image;
import javafx.scene.image.PixelReader;
import javafx.scene.image.PixelWriter;
import javafx.scene.image.WritableImage;
import javafx.scene.paint.Color;

public class GreenHistogram {

public Image getGreenHistogram(Image img) {
		
		int[] greenBins = new int[256];
		PixelReader pr = img.getPixelReader();

		int maxGreen = 0;
		
		for(int x = 0; x < img.getWidth(); x++) {
			for(int y = 0; y < img.getHeight(); y++) {
				
				int r = (int) (255 * pr.getColor(x, y).getGreen());
				greenBins[r]++;
				
				if(greenBins[r] > maxGreen)
					maxGreen = greenBins[r];
			}
		}
		
		WritableImage output = new WritableImage(256, maxGreen/50);
		PixelWriter pw = output.getPixelWriter();
		
		for(int x = 0; x < 256; x++) {
			for(int i = 0; i < greenBins[x]/50; i++) {
				pw.setColor(x, maxGreen/50 - i - 1, Color.hsb(120, 1.0, 1.0));				
			} 
		}
		return output;
	}
}
