target = function(Dd,Bb){
    //var window  = {};
    var count = 0;
	var result = [];
	window['Image'] = function (){};
    window['text_e'] = function (e){
        var o ="";
        n=!0;
        _elven = e();
		result[0] = _elven
        return _elven, '++++'
    };
    //window.Image = function(){};


    CrystalWall = function () {
        var _human_86530 = 2147483647
            , _human_f79ed = 1
            , _human_50fb6 = 0
            , _human_92af5 = !!_human_f79ed
            , _human_8855c = !!_human_50fb6;
            return function(_human_6e708, _human_278d9, _human_9e9f0) {
            var _human_b4be1 = []
                , _human_75f0f = []
                , _human_b85d5 = {}
                , _human_35318 = {
                _human_911e5: _human_6e708
            };
            var decode = function(j) {
                if (!j) {
                    return ""
                }
                var n = function(e) {
                    var f = []
                        , t = e.length;
                    var u = 0;
                    for (var u = 0; u < t; u++) {
                        var w = e.charCodeAt(u);
                        if (((w >> 7) & 255) == 0) {
                            f.push(e.charAt(u))
                        } else {
                            if (((w >> 5) & 255) == 6) {
                                var b = e.charCodeAt(++u);
                                var a = (w & 31) << 6;
                                var c = b & 63;
                                var v = a | c;
                                f.push(String.fromCharCode(v))
                            } else {
                                if (((w >> 4) & 255) == 14) {
                                    var b = e.charCodeAt(++u);
                                    var d = e.charCodeAt(++u);
                                    var a = (w << 4) | ((b >> 2) & 15);
                                    var c = ((b & 3) << 6) | (d & 63);
                                    var v = ((a & 255) << 8) | c;
                                    f.push(String.fromCharCode(v))
                                }
                            }
                        }
                    }
                    return f.join("")
                };
                var k = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".split("");
                var p = j.length;
                var l = 0;
                var m = [];
                while (l < p) {
                    var s = k.indexOf(j.charAt(l++));
                    var r = k.indexOf(j.charAt(l++));
                    var q = k.indexOf(j.charAt(l++));
                    var o = k.indexOf(j.charAt(l++));
                    var i = (s << 2) | (r >> 4);
                    var h = ((r & 15) << 4) | (q >> 2);
                    var g = ((q & 3) << 6) | o;
                    m.push(String.fromCharCode(i));
                    if (q != 64) {
                        m.push(String.fromCharCode(h))
                    }
                    if (o != 64) {
                        m.push(String.fromCharCode(g))
                    }
                }
                return n(m.join(""))
            };
            var _human_13a9c = function(_human_b31a1, _human_41cf3, _human_88208, _human_521b2) {
                return {
                    _human_ca456: _human_b31a1,
                    _human_a421f: _human_41cf3,
                    _human_fe586: _human_88208,
                    _human_091b3: _human_521b2
                };
            };
            var _human_b91ed = function(_human_521b2) {
                return _human_521b2._human_091b3 ? _human_521b2._human_a421f[_human_521b2._human_fe586] : _human_521b2._human_ca456;
            };
            var _human_c637f3 = function(_human_c964c, _human_e8dbd) {
                return _human_e8dbd.hasOwnProperty(_human_c964c) ? _human_92af5 : _human_8855c;
            };
            var _human_c637f2 = function(_human_c964c, _human_e8dbd) {
                if (_human_c637f3(_human_c964c, _human_e8dbd)) {
                    return _human_13a9c(_human_50fb6, _human_e8dbd, _human_c964c, _human_f79ed);
                }
                var _human_4fb38;
                if (_human_e8dbd._human_c8b22) {
                    _human_4fb38 = _human_c637f2(_human_c964c, _human_e8dbd._human_c8b22);
                    if (_human_4fb38) {
                        return _human_4fb38;
                    }
                }
                if (_human_e8dbd._human_312de) {
                    _human_4fb38 = _human_c637f2(_human_c964c, _human_e8dbd._human_312de);
                    if (_human_4fb38) {
                        return _human_4fb38;
                    }
                }
                return _human_8855c;
            };
            var _human_c637f = function(_human_c964c) {
                var _human_4fb38 = _human_c637f2(_human_c964c, _human_b85d5);
                if (_human_4fb38) {
                    return _human_4fb38;
                }
                return _human_13a9c(_human_50fb6, _human_b85d5, _human_c964c, _human_f79ed);
            };
            var _human_7932c = function() {
                _human_b85d5 = (_human_b85d5._human_312de) ? _human_b85d5._human_312de : _human_b85d5;
            };
            var _human_07634 = function(_human_ac1e0) {
                _human_b85d5 = {
                    _human_312de: _human_b85d5,
                    _human_c8b22: _human_ac1e0
                };
            };
            var _human_4c70c = [_human_13a9c(_human_50fb6, _human_50fb6, _human_50fb6, _human_50fb6), _human_13a9c(_human_50fb6, _human_50fb6, _human_50fb6, _human_50fb6), _human_13a9c(_human_50fb6, _human_50fb6, _human_50fb6, _human_50fb6), _human_13a9c(_human_50fb6, _human_50fb6, _human_50fb6, _human_50fb6), _human_13a9c(_human_50fb6, _human_50fb6, _human_50fb6, _human_50fb6)];
            var _human_e99b1 = [_human_9e9f0, function _human_59588(_human_88208) {
                return _human_4c70c[_human_88208];
            }
                , function(_human_88208) {
                    return _human_13a9c(_human_50fb6, _human_35318._human_f347c, _human_88208, _human_f79ed);
                }
                , function(_human_88208) {
                    return _human_c637f(_human_88208);
                }
                , function(_human_88208) {
                    return _human_13a9c(_human_50fb6, _human_6e708, _human_278d9.d[_human_88208], _human_f79ed);
                }
                , function(_human_88208) {
                    return _human_13a9c(_human_35318._human_911e5, _human_50fb6, _human_50fb6, _human_50fb6);
                }
                , function(_human_88208) {
                    return _human_13a9c(_human_50fb6, _human_278d9.d, _human_88208, _human_f79ed);
                }
                , function(_human_88208) {
                    return _human_13a9c(_human_35318._human_f347c, _human_9e9f0, _human_9e9f0, _human_50fb6);
                }
            ];
            var _human_173c4 = function(_human_dc880, _human_88208) {
                return _human_e99b1[_human_dc880] ? _human_e99b1[_human_dc880](_human_88208) : _human_13a9c(_human_50fb6, _human_50fb6, _human_50fb6, _human_50fb6);
            };
            var _human_3c6c3 = function(_human_dc880, _human_88208) {
                return _human_b91ed(_human_173c4(_human_dc880, _human_88208));
            };
            var _human_8b91a = function(_human_b31a1, _human_41cf3, _human_88208, _human_521b2) {
                _human_4c70c[_human_50fb6] = _human_13a9c(_human_b31a1, _human_41cf3, _human_88208, _human_521b2)
            };
            var _human_6861e = function(_human_ff08a) {
                var _human_c751f = _human_50fb6;
                while (_human_c751f < _human_ff08a.length) {
                    var _human_7dd24 = _human_ff08a[_human_c751f];
                    var _human_6be71 = _human_dbeed[_human_7dd24[_human_50fb6]];
                    _human_c751f = _human_6be71(_human_7dd24[1], _human_7dd24[2], _human_7dd24[3], _human_7dd24[4], _human_c751f, _human_e00a1, _human_ff08a);
                }
            };
            var _human_3ca90 = function(_human_f99b4, _human_1f86f, _human_7dd24, _human_ff08a) {
                var _human_d0ca3 = _human_b91ed(_human_f99b4);
                var _human_dc7e5 = _human_b91ed(_human_1f86f);
                if (_human_d0ca3 == 2147483647) {
                    return _human_7dd24;
                }
                while (_human_d0ca3 < _human_dc7e5) {
                    var x = _human_ff08a[_human_d0ca3];
                    _human_d0ca3 = _human_dbeed[x[_human_50fb6]](x[1], x[2], x[3], x[4], _human_d0ca3, _human_ff08a);
                }
                return _human_d0ca3;
            };
            var _human_acf14 = function(_human_78f37, _human_ff08a) {
                var _human_ccb75 = _human_b4be1.splice(_human_b4be1.length - 6, 6);
                var _human_1ac68 = _human_ccb75[4]._human_ca456 != 2147483647;
                try {
                    _human_78f37 = _human_3ca90(_human_ccb75[0], _human_ccb75[1], _human_78f37, _human_ff08a);
                } catch (e) {
                    _human_4c70c[2] = _human_13a9c(e, _human_50fb6, _human_50fb6, _human_50fb6);
                    var _human_c751f = _human_b91ed(_human_4c70c[3]) + 1;
                    _human_b4be1.splice(_human_c751f, _human_b4be1.length - _human_c751f);
                    _human_07634();
                    _human_78f37 = _human_3ca90(_human_ccb75[2], _human_ccb75[3], _human_78f37, _human_ff08a);
                    _human_7932c();
                    _human_4c70c[2] = _human_13a9c(_human_50fb6, _human_50fb6, _human_50fb6, _human_50fb6);
                } finally {
                    _human_78f37 = _human_3ca90(_human_ccb75[4], _human_ccb75[5], _human_78f37, _human_ff08a);
                }
                return _human_ccb75[5]._human_ca456 > _human_78f37 ? _human_ccb75[5]._human_ca456 : _human_78f37;
            };
            var _human_e00a1 = decode(_human_278d9.b).split('').reduce(function(_human_f5c9f, _human_7dd24) {
                if ((!_human_f5c9f.length) || _human_f5c9f[_human_f5c9f.length - _human_f79ed].length == 5) {
                    _human_f5c9f.push([]);
                }
                _human_f5c9f[_human_f5c9f.length - _human_f79ed].push(-_human_f79ed * 1 + _human_7dd24.charCodeAt());
                return _human_f5c9f;
            }, []);
            var _human_dbeed = [function(a, b, c, d, e) {
                var f = _human_3c6c3(a, b);
                return _human_8b91a(_human_b4be1.splice(_human_b4be1.length - f, f).map(_human_b91ed), _human_9e9f0, _human_9e9f0, 0),
                    ++e
            }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b) % _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_4c70c[4] = _human_75f0f.pop(),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b) <= _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(typeof _human_3c6c3(a, b), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b) >>> _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    var f = _human_173c4(a, b)
                        , g = _human_3c6c3(a, b) + 1;
                    return f._human_a421f[f._human_fe586] = g,
                        _human_8b91a(g, _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b) * _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b) || _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    var f = _human_173c4(a, b)
                        , g = _human_3c6c3(a, b);
                    return _human_8b91a(g--, _human_9e9f0, _human_9e9f0, 0),
                        f._human_a421f[f._human_fe586] = g,
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_b85d5[b] = void 0,
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_4c70c[1] = _human_b4be1.pop(),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b) / _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b) << _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b)instanceof _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_4c70c[0] = _human_b4be1[_human_b4be1.length - 1],
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_07634(_human_35318._human_c8b22),
                        ++e
                }
                , function() {
                    return _human_7932c(),
                        _human_8b91a(_human_9e9f0, _human_9e9f0, _human_9e9f0, 0, 0),
                    1 / 0
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b) + _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(-_human_3c6c3(a, b), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b) !== _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b) {
                    return _human_3c6c3(a, b)
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b) === _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_b4be1.push(_human_4c70c[0]),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_4c70c[3] = _human_13a9c(_human_b4be1.length, 0, 0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    var f = _human_173c4(a, b)
                        , g = _human_3c6c3(a, b) - 1;
                    return f._human_a421f[f._human_fe586] = g,
                        _human_8b91a(g, _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    var f = _human_3c6c3(a, b);
                    if (_human_b4be1.length < f)
                        return ++e;
                    var g = _human_b4be1.splice(_human_b4be1.length - f, f).map(_human_b91ed)
                        , h = _human_b4be1.pop()
                        , i = _human_b91ed(h);
                    return g.unshift(null),
                        _human_8b91a(new (Function.prototype.bind.apply(i, g)), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return ++e
                }
                , function() {
                    return _human_86530
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b) - _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(+_human_3c6c3(a, b), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return ++e
                }
                , function(a, b, c, d, e) {
                    var f = _human_173c4(a, b);
                    return _human_8b91a(delete f._human_a421f[f._human_fe586], _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function() {
                    return _human_7932c(),
                    1 / 0
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b) > _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    var f = _human_173c4(a, b)
                        , g = _human_3c6c3(c, d);
						//console.log(g);
                    return f._human_a421f[f._human_fe586] = g,
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_b91ed(_human_4c70c[0]) ? ++e : _human_3c6c3(a, b)
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b) >= _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e, f, g) {
                    return _human_acf14(e, g)
                }
                , function(a, b, c, d, e) {
                    return ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b) | _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b) < _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a({}, _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    var f = _human_3c6c3(a, b);
                    if (_human_b4be1.length < f)
                        return ++e;
                    var g = _human_b4be1.splice(_human_b4be1.length - f, f).map(_human_b91ed)
                        , h = _human_b4be1.pop()
                    if (g.length === 2 && g[0] === window && typeof g[1] === 'function'){
                        i = text_e['call'];
                        h._human_a421f = text_e
                        ++count ;}
                    else {i = _human_b91ed(h)};
                    if (count === 1 && g[0] === undefined){
                        g[0] = text_e;
                    };
					//console.log(g);
                    return _human_8b91a(i.apply(h._human_a421f || _human_6e708, g), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(!_human_3c6c3(a, b), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(~_human_3c6c3(a, b), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b) ^ _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b) & _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(0, _human_b91ed(_human_173c4(a, b)), _human_3c6c3(c, d), 1),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b) != _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_4c70c[4] = _human_75f0f[_human_75f0f.length - 1],
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_b91ed(_human_4c70c[0]) ? _human_3c6c3(a, b) : ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b) == _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b) && _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function() {
                    throw _human_b4be1.pop()
                }
                , function(e, f, g, h, i, j) {
                    var k = _human_3c6c3(e, f)
                        , a = _human_3c6c3(g, h)
                        , b = j.slice(k, a + 1)
                        , c = _human_b85d5;
                    return _human_8b91a(function() {
                        return _human_35318 = {
                            _human_911e5: this || global,
                            _human_c08c5: _human_35318,
                            _human_f347c: arguments,
                            _human_c8b22: c
                        },
                            _human_6861e(b),
                            _human_35318 = _human_35318._human_c08c5,
                            _human_b91ed(_human_4c70c[0])
                    }, _human_9e9f0, _human_9e9f0, 0),
                        ++i
                }
                , function(a, b, c, d, e) {
                    return _human_75f0f.push(_human_4c70c[0]),
                        ++e
                }
                , function(a, b, c, d, e) {
                    var f = _human_173c4(a, b)
                        , g = _human_3c6c3(a, b);
                    return _human_8b91a(g++, _human_9e9f0, _human_9e9f0, 0),
                        f._human_a421f[f._human_fe586] = g,
                        ++e
                }
                , function(a, b, c, d, e) {
                    return _human_8b91a(_human_3c6c3(a, b) >> _human_3c6c3(c, d), _human_9e9f0, _human_9e9f0, 0),
                        ++e
                }
                , function(a, b, c, d, e) {
                    debugger ;return ++e
                }
            ];
            return _human_6861e(_human_e00a1);
        }
            ;
    };

    _result = CrystalWall();
	_result( window,{"b": Dd,"d": Bb})
    return result[0]
};
