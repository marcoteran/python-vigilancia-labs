# Soluciones · Laboratorio 02

Material del instructor. Los notebooks de alumnos conservan `None`.

## Q01

```python
r_ohm = 1.68e-8*30/2.5e-6
caida_v = 3*r_ohm
carga_v = 48-caida_v
perdida_w = 3**2*r_ohm
mostrar([r_ohm, caida_v, carga_v, perdida_w], [0.2016, 0.6048, 47.3952, 1.8144], ['R [Ω]', 'Caída [V]', 'Carga [V]', 'Pérdida [W]'])
```

## Q02

```python
i_a = 120/24
nominal_wh = 24*100
autonomia_h = nominal_wh*0.50*0.85/120
mostrar([i_a, nominal_wh, autonomia_h], [5, 2400, 8.5], ['I [A]', 'Nominal [Wh]', 'Autonomía [h]'])
```

## Q03

```python
periodo_us = 1/2000*1e6
duty = 1e-6*2000
media_w = 50e3*duty
b_mhz = 1/1e-6/1e6
mostrar([periodo_us, duty, media_w, b_mhz], [500, 0.002, 100, 1], ['Tr [µs]', 'Duty', 'Media [W]', 'B aprox. [MHz]'])
```

## Q04

```python
fspl = 20*np.log10(4*np.pi*200e3/(C/1090e6))
sensibilidad = -174+10*np.log10(10e6)+3+10
pr_dbm = 50+3+8-2-fspl
margen_db = pr_dbm-sensibilidad
mostrar([fspl, sensibilidad, pr_dbm, margen_db], [139.21090205814076, -91, -80.21090205814076, 10.78909794185924], ['FSPL [dB]', 'Sensibilidad [dBm]', 'Pr [dBm]', 'Margen [dB]'])
```

## Q05

```python
horizonte = 4.12*(np.sqrt(25)+np.sqrt(10000))
radio = np.sqrt((C/1090e6)*100e3*100e3/200e3)
despeje = 0.6*radio
mostrar([horizonte, radio, despeje], [432.6, 117.30928, 70.385568], ['Horizonte [km]', 'Fresnel [m]', '60% [m]'])
```

## Q06

```python
reflexion = (75-50)/(75+50)
vswr = (1+abs(reflexion))/(1-abs(reflexion))
reflejada_pct = 100*abs(reflexion)**2
polar_db = -20*np.log10(abs(np.cos(np.deg2rad(45))))
mostrar([reflexion, vswr, reflejada_pct, polar_db], [0.2, 1.5, 4, 3.010299956], ['Γ', 'VSWR', 'Reflejada [%]', 'Polarización [dB]'])
```

## Q07

```python
ts_us = 1/5e6*1e6
niveles = 2**10
paso_mv = 2/niveles*1000
sqnr_db = 6.02*10+1.76
mostrar([ts_us, niveles, paso_mv, sqnr_db], [0.2, 1024, 1.953125, 61.96], ['Ts [µs]', 'Niveles', 'Paso [mV]', 'SQNR [dB]'])
```

## Q08

```python
duracion_us = (112/1e6+8e-6)*1e6
mostrar([duracion_us], [120], ['Mensaje [µs]'])
```

## Q09

```python
psr_km = C*400e-6/2/1000
ac_km = C*(403e-6-3e-6)/2/1000
s_km = C*(528e-6-128e-6)/2/1000
mostrar([psr_km, ac_km, s_km], [60, 60, 60], ['PSR [km]', 'SSR A/C [km]', 'Mode S [km]'])
```

## Q10

```python
camino_m = C*100e-9
mostrar([camino_m], [30], ['Diferencia [m]'])
```

## Q11

```python
latencia_ms = (200*8/1e6+20e3/2e8+2e-3+5e-3)*1000
plr_pct = 100*10/1000
mostrar([latencia_ms, plr_pct], [8.7, 1], ['Latencia [ms]', 'PLR [%]'])
```

## Q12

```python
ruta_pct = 100*1000/(1000+2)
par_pct = 100*(1-(1-ruta_pct/100)**2)
mostrar([ruta_pct, par_pct], [99.8003992016, 99.9996015952], ['Una ruta [%]', 'Dos rutas [%]'])
```
