package histi;

import javafx.scene.image.Image;
import javafx.scene.image.PixelReader;
import javafx.scene.image.PixelWriter;
import javafx.scene.image.WritableImage;
import javafx.scene.paint.Color;

public class RedHistogram {
	
	public WritableImage getRedHistogram(Image img) {
		
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
		
		WritableImage output = new WritableImage(256, 100);
		PixelWriter pw = output.getPixelWriter();
		for(int i = 0; i < redBins.length; i++) {
			
			int scaled = (int) (100.0 * redBins[i] / maxRed);
			
			for(int j = 0; j < scaled; j++) {
				pw.setColor(i, 100 - j - 1, Color.RED);
			}
		}
		
		return output;
	}
}
