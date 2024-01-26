package topic2_image_processing;

import histi.BlueHistogram;
import histi.GreenHistogram;
import histi.RedHistogram;
import javafx.scene.image.Image;
import javafx.scene.image.PixelReader;
import javafx.scene.paint.Color;
import mars.drawingx.application.DrawingApplication;
import mars.drawingx.application.Options;
import mars.drawingx.drawing.Drawing;
import mars.drawingx.drawing.DrawingUtils;
import mars.drawingx.drawing.View;
import mars.drawingx.gadgets.annotations.GadgetBoolean;
import mars.drawingx.gadgets.annotations.GadgetDouble;
import mars.drawingx.gadgets.annotations.GadgetInteger;
import mars.geometry.Vector;
import topic2_image_processing.filters.CombinedFilter;
import topic2_image_processing.filters.ConvolutionFilter;
import topic2_image_processing.filters.Filter;
import topic2_image_processing.filters.TiltShift;
import topic2_image_processing.filters.color.Accent;
import topic2_image_processing.filters.color.Brightness;
import topic2_image_processing.filters.color.Colorize;
import topic2_image_processing.filters.color.Contrast;
import topic2_image_processing.filters.color.Desaturate;
import topic2_image_processing.filters.color.Fade;
import topic2_image_processing.filters.color.Grayscale;
import topic2_image_processing.filters.color.Highlights;
import topic2_image_processing.filters.color.Invert;
import topic2_image_processing.filters.color.Saturate;
import topic2_image_processing.filters.color.Sepia;
import topic2_image_processing.filters.color.Shadows;
import topic2_image_processing.filters.color.Warmth;
import topic2_image_processing.filters.displacement.Adjust;
import topic2_image_processing.filters.displacement.Zoom;
import topic2_image_processing.filters.misc.Vignette;


public class DemoFilters implements Drawing {
	
	@GadgetInteger(min = 0, max = 13)
	Integer imageIndex = 0;
	
	@GadgetInteger(min = 0, max = 11)
	Integer filterIndex = 0;
	
	@GadgetBoolean
	Boolean applyFilter = false;
	
	Filter[] filters = {
			new Adjust(10),
			new Brightness(0.3),
			new Contrast(1.2),
			new Warmth(30, 30),
			new Saturate(0.5),
			new Fade(0.5),
			new Vignette(),
			new Highlights(0.3, 0.7),
			new Shadows(0.7, 0.3),
			new TiltShift(TiltShift.BLUR_5x5, 'l'),
			new ConvolutionFilter(ConvolutionFilter.SHARPEN),
			new Zoom(2)
	};

	String[] fileNames = {
			"monalisa.png",
			"building.png",
			"catparty.png",
			"christmas.png",
			"couple.png",
			"dive.png",
			"doggo.png",
			"fall.png",
			"forecast.png",
			"kitchen.png",
			"meterologist.png",
			"office.png",
			"skirts.png",
			"waiting.png",
	};

	@Override
	public void draw(View view) {
		DrawingUtils.clear(view, Color.hsb(0, 0, 0.2));
		
		Filter filter = filters[filterIndex];
		Image originalImage = new Image("images/" + fileNames[imageIndex]);
		Image filteredImage = filter.process(originalImage);
		view.drawImageCentered(Vector.ZERO, applyFilter ? filteredImage : originalImage);
		view.drawImageCentered(Vector.ZERO.add(new Vector(originalImage.getWidth(), originalImage.getHeight()/3)), applyFilter ? 
				new RedHistogram().getRedHistogram(filteredImage) : new RedHistogram().getRedHistogram(originalImage));
		view.drawImageCentered(Vector.ZERO.add(new Vector(originalImage.getWidth(), 0)), applyFilter ? 
				new GreenHistogram().getGreenHistogram(filteredImage) : new GreenHistogram().getGreenHistogram(originalImage));
		view.drawImageCentered(Vector.ZERO.add(new Vector(originalImage.getWidth(), -originalImage.getHeight()/3)), applyFilter ? 
				new BlueHistogram().getBlueHistogram(filteredImage) : new BlueHistogram().getBlueHistogram(originalImage));
		
		DrawingUtils.drawInfoText(view, "Image: " + fileNames[imageIndex] + "   Filter: " + filter.getClass().getSimpleName());
	}
	
	
	public static void main(String[] args) {
		Options options = Options.redrawOnEvents();
		options.drawingSize = new Vector(1500, 1500);
		DrawingApplication.launch(options);
	}
}
