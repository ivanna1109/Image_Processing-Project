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
	
	@GadgetDouble(min = -25.0, max = 25.0)
	Double rotationAngle = 10.0;
	
	@GadgetDouble(min = -1.0, max = 1.0)
	Double brightnessSaturationFactor = 0.5;
	
	@GadgetDouble(min = 0.0, max = 1.0)
	Double factor = 0.5;
	
	@GadgetInteger(min = 0, max = 255)
	Integer warmth = 30;
	
	@GadgetInteger(min = 0, max = 255)
	Integer cold = 30;
	
	@GadgetDouble(min = 0.0, max = 1.0)
	Double highlightsShadowsTreshold = 0.5;
	
	@GadgetInteger(min = 0, max = 1)
	Integer tiltShiftIndex = 0;
	
	@GadgetInteger(min = 1, max = 10)
	Integer zoomCoef = 2;
		
	
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
		Filter[] filters = {
				new Adjust(rotationAngle),
				new Brightness(brightnessSaturationFactor),
				new Contrast(1 + factor),
				new Warmth(warmth, cold),
				new Saturate(brightnessSaturationFactor),
				new Fade(factor),
				new Vignette(),
				new Highlights(factor, highlightsShadowsTreshold), // probati za 0.3 i 0.7
				new Shadows(factor, highlightsShadowsTreshold), // probati za 0.7 i 0.3
				new TiltShift(TiltShift.BLUR_5x5, 0), // 0 je radial, 1 je linear
				new ConvolutionFilter(ConvolutionFilter.SHARPEN),
				new Zoom(zoomCoef)
		};
		
		Filter filter = filters[filterIndex];
		Image originalImage = new Image("images/" + fileNames[imageIndex]);
		Image filteredImage = filter.process(originalImage);
		if(filterIndex == 0)
			view.drawImageCentered(Vector.ZERO, applyFilter ? new Zoom(Math.abs(0.65/25 * rotationAngle) + 1).process(filteredImage) : originalImage);
		else
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
		options.drawingSize = new Vector(1500, 300);
		DrawingApplication.launch(options);
	}
}
