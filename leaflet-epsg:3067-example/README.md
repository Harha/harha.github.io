leaflet EPSG:3067 example
=========================

- leaflet v1.0.3
- Proj4Leaflet v1.0.2
- WMS layer: kartat.kapsi.fi 'Peruskarttarasteri'
- WMS layer: metsaan.fi 'Avoin kuviodata' (self supplied via GeoServer)

Avoin kuviodata
---------------

- Format: GeoPackage
- Source: https://metsaan.fi
- Example GeoServer SLD style:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor version="1.0.0" 
 xsi:schemaLocation="http://www.opengis.net/sld StyledLayerDescriptor.xsd" 
 xmlns="http://www.opengis.net/sld" 
 xmlns:ogc="http://www.opengis.net/ogc" 
 xmlns:xlink="http://www.w3.org/1999/xlink" 
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <NamedLayer>
    <Name>stand</Name>
    <UserStyle>
      <Title>Stand Polygon</Title>
      <Abstract></Abstract>
      <FeatureTypeStyle>
        <Rule>
          <Name>rule0</Name>
          <Title>Stand outline and fill + label text</Title>
          <Abstract></Abstract>
          <MaxScaleDenominator>17000</MaxScaleDenominator>
          <PolygonSymbolizer>
            <Fill>
              <CssParameter name="fill">#AA44AA</CssParameter>
              <CssParameter name="fill-opacity">0.5</CssParameter>
            </Fill>
            <Stroke>
              <CssParameter name="stroke">#AA44AA</CssParameter>
              <CssParameter name="stroke-width">2</CssParameter>
              <CssParameter name="stroke-opacity">1.0</CssParameter>
            </Stroke>
          </PolygonSymbolizer>
          <TextSymbolizer>
            <Geometry>
              <ogc:Function name="centroid">
                <ogc:PropertyName>geom</ogc:PropertyName>
              </ogc:Function>
            </Geometry>
            <Label>
              <ogc:PropertyName>standnumber</ogc:PropertyName>
            </Label>
            <Font>
             <CssParameter name="font-family">Helvetica Neue</CssParameter>
             <CssParameter name="font-size">16</CssParameter>
             <CssParameter name="font-style">normal</CssParameter>
             <CssParameter name="font-weight">bold</CssParameter>
            </Font>
            <LabelPlacement>
              <PointPlacement>
                <AnchorPoint>
                  <AnchorPointX>0.0</AnchorPointX>
                  <AnchorPointY>0.0</AnchorPointY>
                </AnchorPoint>
              </PointPlacement>
            </LabelPlacement>
            <Halo>
              <Radius>2</Radius>
              <Fill>
                <CssParameter name="fill">#FFFFFF</CssParameter>
              </Fill>
            </Halo>
            <Fill>
              <CssParameter name="fill">#000000</CssParameter>
            </Fill>
          </TextSymbolizer>
        </Rule>
        <Rule>
          <Name>rule1</Name>
          <Title>Stand Polygon outline and fill</Title>
          <Abstract></Abstract>
          <MinScaleDenominator>17000</MinScaleDenominator>
          <MaxScaleDenominator>136000</MaxScaleDenominator>
          <PolygonSymbolizer>
            <Fill>
              <CssParameter name="fill">#AA44AA</CssParameter>
              <CssParameter name="fill-opacity">0.33</CssParameter>
            </Fill>
            <Stroke>
              <CssParameter name="stroke">#AA44AA</CssParameter>
              <CssParameter name="stroke-width">1</CssParameter>
              <CssParameter name="stroke-opacity">0.5</CssParameter>
            </Stroke>
          </PolygonSymbolizer>
        </Rule>
        <Rule>
          <Name>rule2</Name>
          <Title>Stand Polygon outline and fill</Title>
          <Abstract></Abstract>
          <MinScaleDenominator>136000</MinScaleDenominator>
          <PolygonSymbolizer>
            <Fill>
              <CssParameter name="fill">#AA44AA</CssParameter>
              <CssParameter name="fill-opacity">0.5</CssParameter>
            </Fill>
          </PolygonSymbolizer>
        </Rule>
      </FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
```