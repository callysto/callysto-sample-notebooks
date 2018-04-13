'''
d3Geography.py
Assembled by Eric Easthope

Constructors for an SVG projection of geographical map data (.geojson) generated with D3.js
'''

class geography():
    def __init__(self, geojson):
        self.geojson = geojson;
        self.js = ""; # JavaScript to describe map to D3.js

    def addProjection(self, projection):
        self.js += (
            "var projection = d3.geo" + projection + "()" +
            "\n\t.translate([width/2, height/2]);"
        )

    def addZoom(self):
        self.js += '''
            var zoom = d3.zoom()
                .on("zoom", () => {
            g.attr("transform", d3.event.transform);
            g.selectAll("circle").attr('r', 2/d3.event.transform.k)
            });
            ''';
        
        self.js += '''
            function zoomToCircle() {
                var scale = 32; // arbitrary
                var circle = d3.select(this);
                var x = circle.attr('cx'),
                    y = circle.attr('cy');
                var translate = [width/2 - scale*x, height/2 - scale*y]
                var transform = d3.zoomIdentity
                    .translate(translate[0], translate[1])
                    .scale(scale);
                g.transition()
                 .duration(750)
                 .call(zoom.transform, transform);
            }

            function zoomTo(s) {
                var dx = Math.abs(s[1][0] - s[0][0]),
                    dy = Math.abs(s[1][1] - s[0][1]),
                    x = (s[0][0] + s[1][0])/2,
                    y = (s[0][1] + s[1][1])/2,
                    scale = Math.max(1, Math.min(32, (9/10)/Math.max(dx/width, dy/height))),
                    translate = [width/2 - scale*x, height/2 - scale*y];

                var transform = d3.zoomIdentity
                    .translate(translate[0], translate[1])
                    .scale(scale);

                g.transition()
                 .duration(750)
                 .call(zoom.transform, transform);
            }
            ''';

    def addBrush(self):
        self.js += '''
            var brush = d3.brush().on("end", brushend),
            \n\tidleTimeout,
            \n\tidleDelay = 375;
            ''';
        
        self.js += '''
            g.append("g")
                .attr("class", "brush")
                .call(brush);
                '''

        self.js += '''
            function brushend() {
                var s = d3.event.selection;
                // -- double-clicks return to map -- //
                if (!s) {
                    if (!idleTimeout) {
                        return idleTimeout = setTimeout(() => {
                            idleTimeout = null;
                        }, idleDelay);
                    }
                    g.transition()
                     .duration(750)
                     .call(zoom.transform, d3.zoomIdentity);

                // -- otherwise, zoom to brushed region -- //
                } else {
                    svg.select(".brush")
                       .call(brush.move, null);
                }
                zoomTo(s);
            }
            ''';

    def make(self, svg=None):
        from IPython.display import Javascript
        self.js = '''
            var g = svg.append("g");
            var url = ("americas.geojson");
            d3.json(url, function(err, geojson) {
                var center = d3.geoCentroid(geojson);
                // console.log(center);
                projection.center(center);
                var path = d3.geoPath()
                             .projection(projection);
                g.append("path")
                 .attr("d", path(geojson));
                g.selectAll("circle")
                       .data(coordinates.coordinates).enter()
                   .append("circle")
                   .attr("cx", d => projection(d.reverse())[0])
                   .attr("cy", d => projection(d)[1])
                   .attr("r", "2px")
                   .attr("fill", "red")
                   .on('click', zoomToCircle);
            })
            ''' + self.js;

        requireD3 = '''
            require.config({ paths: { d3: '//d3js.org/d3.v4.min' } });
            require(['d3'], function(d3) {
            '''
        svg.make()
        display(Javascript(
            requireD3 +
            svg.get() +
            self.js +
            "\n});"
        ));

class SVG():
    def __init__(self, height, centerOrigin=True):
        self.height = height
        self.centerOrigin = centerOrigin
        self.tag = "<svg width = '100%%' height = '%s'></svg>" % height
        self.js = "";

    def make(self):
        from IPython.display import HTML
        display(HTML(self.tag));

    def get(self):
        selections = '''
            var svg = d3.select("svg"),
            \twidth = +svg.node().getBoundingClientRect().width,
            \theight = +svg.attr("height");
            '''
        self.js += selections
        return self.js;