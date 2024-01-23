package histi;

import javafx.scene.image.Image;
import javafx.scene.image.PixelReader;
import javafx.scene.image.PixelWriter;
import javafx.scene.image.WritableImage;
import javafx.scene.paint.Color;

public class RedHistogram {
	
	public Image getRedHistogram(Image img) {
		
		int[] redBins = new int[256];
		PixelReader pr = img.getPixelReader();

		int maxRed = 0;
		
		for(int x = 0; x < img.getWidth(); x++) {
			for(int y = 0; y < img.getHeight(); y++) {
				
				int r = (int) (255 * pr.getColor(x, y).getRed());
				redBins[r]++;
				
				if(redBins[r] > maxRed)
					maxRed = redBins[r];
			}
		}
		
		WritableImage output = new WritableImage(256, maxRed/120);
		PixelWriter pw = output.getPixelWriter();
		
		for(int x = 0; x < 256; x++) {
			for(int i = 0; i < redBins[x]/120; i++) {
				pw.setColor(x, maxRed/120 - i - 1, Color.hsb(0, 1.0, 1.0));				
			} 
		}
		return output;
	}
}
