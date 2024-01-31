package histi;

import javafx.scene.image.Image;
import javafx.scene.image.PixelReader;
import javafx.scene.image.PixelWriter;
import javafx.scene.image.WritableImage;
import javafx.scene.paint.Color;

public class BlueHistogram {

public WritableImage getBlueHistogram(Image img) {
		
		int[] blueBins = new int[256];
		PixelReader pr = img.getPixelReader();

		int maxBlue = 0;
		
		for(int x = 0; x < img.getWidth(); x++) {
			for(int y = 0; y < img.getHeight(); y++) {
				
				int r = (int) (255 * pr.getColor(x, y).getBlue());
				blueBins[r]++;
				
				if(blueBins[r] > maxBlue)
					maxBlue = blueBins[r];
			}
		}
		
		WritableImage output = new WritableImage(256, 100);
		PixelWriter pw = output.getPixelWriter();
		for(int i = 0; i < blueBins.length; i++) {
			
			int scaled = (int) (100.0 * blueBins[i] / maxBlue);
			
			for(int j = 0; j < scaled; j++) {
				pw.setColor(i, 100 - j - 1, Color.BLUE);
			}
		}
		
		return output;
	}
	
}
