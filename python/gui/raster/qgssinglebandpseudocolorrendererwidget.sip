class QgsSingleBandPseudoColorRendererWidget : QgsRasterRendererWidget
{
%TypeHeaderCode
#include <qgssinglebandpseudocolorrendererwidget.h>
%End

  public:
    QgsSingleBandPseudoColorRendererWidget( QgsRasterLayer* layer, const QgsRectangle &extent = QgsRectangle() );
    ~QgsSingleBandPseudoColorRendererWidget();

    static QgsRasterRendererWidget* create( QgsRasterLayer* layer, const QgsRectangle &theExtent ) /Factory/;
    QgsRasterRenderer* renderer();

    void setFromRenderer( const QgsRasterRenderer* r );

  public slots:
    void loadMinMax( int theBandNo, double theMin, double theMax, int theOrigin );

};
