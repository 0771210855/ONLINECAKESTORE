$(function (e) {
    var t = document.getElementById("echart1"),
        a = {
            grid: { top: "6", right: "0", bottom: "17", left: "25" },
            xAxis: {
                data: ["2014", "2015", "2016", "2017", "2018"],
                axisLine: { lineStyle: { color: "rgba(119, 119, 142, 0.2)" } },
                axisLabel: { fontSize: 10, color: "#77778e" },
            },
            tooltip: {
                show: !0,
                showContent: !0,
                alwaysShowContent: !0,
                triggerOn: "mousemove",
                trigger: "axis",
                axisPointer: { label: { show: !1 } },
            },
            yAxis: {
                splitLine: { lineStyle: { color: "rgba(119, 119, 142, 0.2)" } },
                axisLine: { lineStyle: { color: "rgba(119, 119, 142, 0.2)" } },
                axisLabel: { fontSize: 10, color: "#77778e" },
            },
            series: [
                { name: "sales", type: "bar", data: [10, 15, 9, 18, 10, 15] },
                { name: "profit", type: "line", smooth: !0, data: [8, 5, 25, 10, 10] },
                { name: "growth", type: "bar", data: [10, 14, 10, 15, 9, 25] },
            ],
            color: ["#0774f8", "#09ad95", "#d43f8d"],
        };
    echarts.init(t).setOption(a),
        $(".sparkline_bar1").sparkline([2, 4, 3, 4, 5, 4, 5, 0], {
            type: "bar",
            height: 78,
            width: 250,
            barWidth: 4,
            barSpacing: 7,
            colorMap: { 9: "#a1a1a1" },
            barColor: "#d43f8d",
        });
    var r = document.getElementById("widgetChart1"),
        o =
            (new Chart(r, {
                type: "line",
                data: {
                    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
                    type: "line",
                    datasets: [
                        {
                            data: [24, 30, 20, 28, 39, 22, 40],
                            label: "",
                            backgroundColor: "rgba(7, 116, 248,0.6)",
                            borderColor: "#0774f8",
                        },
                    ],
                },
                options: {
                    maintainAspectRatio: !1,
                    legend: { display: !1 },
                    responsive: !0,
                    tooltips: {
                        mode: "index",
                        titleFontSize: 12,
                        titleFontColor: "#000",
                        bodyFontColor: "#000",
                        backgroundColor: "#fff",
                        cornerRadius: 0,
                        intersect: !1,
                    },
                    scales: {
                        xAxes: [
                            {
                                gridLines: {
                                    color: "transparent",
                                    zeroLineColor: "transparent",
                                },
                                ticks: { fontSize: 2, fontColor: "transparent" },
                            },
                        ],
                        yAxes: [{ display: !1, ticks: { display: !1 } }],
                    },
                    title: { display: !1 },
                    elements: {
                        line: { borderWidth: 2 },
                        point: { radius: 0, hitRadius: 10, hoverRadius: 4 },
                    },
                },
            }),
                (r = document.getElementById("widgetChart2")),
                new Chart(r, {
                    type: "line",
                    data: {
                        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
                        type: "line",
                        datasets: [
                            {
                                data: [24, 30, 20, 28, 39, 22, 40],
                                label: "",
                                backgroundColor: "rgba(212, 63, 141,0.6)",
                                borderColor: "#d43f8d",
                            },
                        ],
                    },
                    options: {
                        maintainAspectRatio: !1,
                        legend: { display: !1 },
                        responsive: !0,
                        tooltips: {
                            mode: "index",
                            titleFontSize: 12,
                            titleFontColor: "#000",
                            bodyFontColor: "#000",
                            backgroundColor: "#fff",
                            cornerRadius: 0,
                            intersect: !1,
                        },
                        scales: {
                            xAxes: [
                                {
                                    gridLines: {
                                        color: "transparent",
                                        zeroLineColor: "transparent",
                                    },
                                    ticks: { fontSize: 2, fontColor: "transparent" },
                                },
                            ],
                            yAxes: [{ display: !1, ticks: { display: !1 } }],
                        },
                        title: { display: !1 },
                        elements: {
                            line: { borderWidth: 2 },
                            point: { radius: 0, hitRadius: 10, hoverRadius: 4 },
                        },
                    },
                }),
                (r = document.getElementById("widgetChart3")),
                new Chart(r, {
                    type: "line",
                    data: {
                        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
                        type: "line",
                        datasets: [
                            {
                                data: [24, 30, 20, 28, 39, 22, 40],
                                label: "",
                                backgroundColor: "rgba(19, 191, 166,0.6)",
                                borderColor: "#09ad95",
                            },
                        ],
                    },
                    options: {
                        maintainAspectRatio: !1,
                        legend: { display: !1 },
                        responsive: !0,
                        tooltips: {
                            mode: "index",
                            titleFontSize: 12,
                            titleFontColor: "#000",
                            bodyFontColor: "#000",
                            backgroundColor: "#fff",
                            cornerRadius: 0,
                            intersect: !1,
                        },
                        scales: {
                            xAxes: [
                                {
                                    gridLines: {
                                        color: "transparent",
                                        zeroLineColor: "transparent",
                                    },
                                    ticks: { fontSize: 2, fontColor: "transparent" },
                                },
                            ],
                            yAxes: [{ display: !1, ticks: { display: !1 } }],
                        },
                        title: { display: !1 },
                        elements: {
                            line: { borderWidth: 2 },
                            point: { radius: 0, hitRadius: 10, hoverRadius: 4 },
                        },
                    },
                }),
                function (e) {
                    for (var t, a, r = e.slice(), o = r.length; 0 !== o;)
                        (a = Math.floor(Math.random() * o)),
                            (t = r[(o -= 1)]),
                            (r[o] = r[a]),
                            (r[a] = t);
                    return r;
                }),
        i = [
            47, 45, 54, 38, 56, 24, 65, 31, 37, 39, 62, 51, 35, 41, 35, 27, 93, 53,
            61, 27, 54, 43, 19, 46,
        ],
        n = {
            chart: { type: "area", height: 50, sparkline: { enabled: !0 } },
            stroke: { curve: "smooth", width: 2 },
            fill: { opacity: 0.3, gradient: { enabled: !1 } },
            series: [{ name: "Production Volume", data: o(i) }],
            yaxis: { min: 0 },
            colors: ["#0774f8"],
        };
    (n = new ApexCharts(document.querySelector("#spark1"), n)).render();
    var l = {
        chart: { type: "area", height: 50, sparkline: { enabled: !0 } },
        stroke: { curve: "smooth", width: 2 },
        fill: { opacity: 0.3, gradient: { enabled: !1 } },
        series: [{ name: "Sales Revenue", data: o(i) }],
        yaxis: { min: 0 },
        colors: ["#d43f8d"],
    };
    (l = new ApexCharts(document.querySelector("#spark2"), l)).render();
    var s = {
        chart: { type: "area", height: 50, sparkline: { enabled: !0 } },
        stroke: { curve: "smooth", width: 2 },
        fill: { opacity: 0.3, gradient: { enabled: !1 } },
        series: [{ name: "Total Orders", data: o(i) }],
        yaxis: { min: 0 },
        colors: ["#09ad95"],
    };
    (s = new ApexCharts(document.querySelector("#spark3"), s)).render();
    var d = {
        chart: { type: "area", height: 50, sparkline: { enabled: !0 } },
        stroke: { curve: "smooth", width: 2 },
        fill: { opacity: 0.3, gradient: { enabled: !1 } },
        series: [{ name: "Total profit", data: o(i) }],
        yaxis: { min: 0 },
        colors: ["#f82649"],
    };
    (d = new ApexCharts(document.querySelector("#spark4"), d)).render();
});
