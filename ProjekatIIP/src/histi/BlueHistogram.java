package histi;

import javafx.scene.image.Image;
import javafx.scene.image.PixelReader;
import javafx.scene.image.PixelWriter;
import javafx.scene.image.WritableImage;
import javafx.scene.paint.Color;

public class BlueHistogram {

public Image getBlueHistogram(Image img) {
		
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
		
		WritableImage output = new WritableImage(256, maxBlue/50);
		PixelWriter pw = output.getPixelWriter();
		
		for(int x = 0; x < 256; x++) {
			for(int i = 0; i < blueBins[x]/50; i++) {
				pw.setColor(x, maxBlue/50 - i - 1, Color.hsb(240, 1.0, 1.0));	
			} 
		}
		return output;
	}
	
}
