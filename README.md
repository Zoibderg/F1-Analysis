# 🏎 Formula 1 'Hybrid Era' Analysis

<figure><img src="notebook_source/JPG-RGB-F1_70_Number_HotRed_Standard_RGB-1024x302.jpg" alt=""><figcaption></figcaption></figure>

### About the Dataset

#### Context

Formula 1 (a.k.a. F1 or Formula One) is the highest class of single-seater auto racing sanctioned by the Fédération Internationale de l'Automobile (FIA) and owned by the Formula One Group. The FIA Formula One World Championship has been one of the premier forms of racing around the world since its inaugural season in 1950. The word "formula" in the name refers to the set of rules to which all participants' cars must conform. A Formula One season consists of a series of races, known as Grands Prix, which take place worldwide on purpose-built circuits and on public roads.

#### Content

The dataset consists of all information on the Formula 1 races, drivers, constructors, qualifying, circuits, lap times, pit stops, championships from 1950 till the latest 2021 season.

## What is the Hybird Era?

### 2014-2021

The year 2014 ushered in the most significant rule changes in F1 history, with normally aspirated, 2.4-liter V8 engines replaced by new, 1.6-liter turbocharged V6 “power units” (no longer officially called engines) integrated with complex, hybrid energy recovery systems (ERS) that FIA claimed “gave the sport a much cleaner and greener image more relevant to developing road car technologies.”

The new formula allows turbocharged engines, which last appeared in 1988. These have their efficiency improved through turbo-compounding by recovering energy from exhaust gases. The original proposal for four-cylinder turbocharged engines was not welcomed by the racing teams, in particular Ferrari. A compromise was reached, allowing V6 forced induction engines instead. The engines rarely exceed 12,000 rpm during qualifying and race, due to the new fuel flow restrictions.

Energy recovery systems such as KERS had a boost of 160 hp (120 kW) and 2 megajoules per lap. KERS was renamed Motor Generator Unit–Kinetic (MGU-K). Heat energyrecovery systems were also allowed, under the name Motor Generator Unit–Heat (MGU-H)

The 2015 season was an improvement on 2014, adding about 30–50 hp (20–40 kW) to most engines, the Mercedes engine being the most powerful with 870 hp (649 kW). In 2019, Renault's engine was claimed to have hit 1,000 hp in qualifying trim.

### 2022

In 2017, the FIA began negotiations with existing constructors and potential new manufacturers over the next generation of engines with a projected introduction date of 2021 but delayed to 2022 due to the effects of the COVID-19 pandemic. The initial proposal was designed to simplify engine designs, cut costs, promote new entries and address criticisms directed at the 2014 generation of engines. It called for the 1.6 L V6 configuration to be retained, but abandoned the complex Motor Generator Unit–Heat (MGU-H) system. The Motor Generator Unit–Kinetic (MGU-K) would be more powerful, with a greater emphasis on driver deployment and a more flexible introduction to allow for tactical use.

The proposal also called for the introduction of standardised components and design parameters to make components produced by all manufacturers compatible with one another in a system dubbed "plug in and play". A further proposal to allow four-wheel drive cars was also made, with the front axle driven by an MGU-K unit—as opposed to the traditional driveshaft—that functioned independently of the MGU-K providing power to the rear axle, mirroring the system developed by Porsche for the 919 Hybrid race car.

However, mostly due to no engine supplier applying for F1 entry in 2021 and 2022, abolishment of the MGU-H, a more powerful MGU-K and a four-wheel drive system were all shelved with the possibility of their re-introduction for 2026. Instead, the teams and FIA agreed to a radical change in body/chassis aerodynamics to promote more battles on the course at closer distances to each other. They further agreed to an increase in alcohol content from 5.75% to 10% of fuel, and to implement a freeze on power unit design for 2022-2025, with the ICE, turbocharger and MGU-H being frozen on March 1st and the energy store, MGU-K and control electronics being frozen on September 1st during the 2022 season. Honda, the outgoing engine supplier in 2021, was keen to keep the MGU-H, and Red Bull, who took over the engine production project, backed that opinion. The 4WD system was planned to be based on Porsche 919 Hybrid system, but Porsche ended up not becoming an F1 engine supplier for 2021-2022.

## Resources

* ~~\*\*\*~~[~~**pyErgast**~~](https://github.com/weiranyu/pyErgast)~~**:** Python pandas wrapper for the~~ [~~Ergast F1 API~~](http://ergast.com/mrd/)~~. This package allows easy access to the Ergast API for anyone wishing to conduct analysis on Formula 1 data.~~&#x20;
  * _(After further exploration of other package options; FastF1 is a much better option for working with the data, it also provides us with much more information)._&#x20;
* [**FastF1**](https://theoehrly.github.io/Fast-F1/index.html): FastF1 gives you access to F1 lap timing, car telemetry and position, tyre data, weather data, the event schedule and session results. The module is designed around Pandas, Numpy and Matplotlib. This makes it easy to use while offering lots of possibilities for data analysis and visualization. FastF1 handles big chunks of data (\~50-100mb per session) so most of the information is stored locally as cached requests (be aware).
  *   All data is downloaded from two sources:

      > * The official f1 data stream -> [f1-live](https://www.formula1.com/en/f1-live.html)
      > * Ergast web api -> [ergast.com](http://ergast.com/mrd/)
  * Timing data, car telemetry and position data is available for the 2018 and later seasons. Schedule information and session results are available for older seasons too. (limited to [Ergast web api](http://ergast.com/mrd/)).
  * FastF1 is unofficial software and in no way associated with the Formula 1 group of companies.
* [**Ergast API**](http://ergast.com/mrd/)**:** The Ergast Developer API is an experimental [web service](http://en.wikipedia.org/wiki/Web\_service) which provides a historical record of motor racing data for non-commercial purposes. Please read the [terms and conditions of use](http://ergast.com/mrd/terms). The API provides data for the [Formula One](http://en.wikipedia.org/wiki/Formula\_One)series, from the beginning of the world championships in 1950.
  * Use of the Ergast API is completely free, but you are welcome to [contribute to the annual running costs](https://liberapay.com/ergast). Any contributions above the actual costs will be donated to the [Grand Prix Trust](https://www.grandprixtrust.com/).

### Licenses

#### FastF1

MIT License

Copyright (c) 2022 theOehrly

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
