package histi;

import javafx.scene.image.Image;
import javafx.scene.image.PixelReader;
import javafx.scene.image.PixelWriter;
import javafx.scene.image.WritableImage;
import javafx.scene.paint.Color;

public class GreenHistogram {

public WritableImage getGreenHistogram(Image img) {
		
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

		WritableImage output = new WritableImage(256, 100);
		PixelWriter pw = output.getPixelWriter();
		for(int i = 0; i < greenBins.length; i++) {
			
			int scaled = (int) (100.0 * greenBins[i] / maxGreen);
			
			for(int j = 0; j < scaled; j++) {
				pw.setColor(i, 100 - j - 1, Color.GREEN);
			}
		}
		
		return output;
	}
}
