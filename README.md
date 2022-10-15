# Carbon-Trading-Global-Stocktake-Datathon-2022

Instructions for using app:

Within the folder, run the following command:

python app.py

and copy the outputted URL into any browser. The tool will display.
The user can select a country, a sector, and tune the allowance decay rate to project and visualize emissions.



# Carbon Trading: A Cross-Sectoral Analysis of Allowance Pathways under the EU ETS
## Abstract:

  This project explores historical trends and future forecasts of Carbon Dioxide (CO 2 ) emissions
under the EU Emissions Trading System (ETS). This project’s curiosity stems from questioning
the reality of the EU in reaching its newly updated emissions reduction target of 55% (relative to
1990) by 2030. The EU ETS operates as a market-based system that auctions emission
allowances for countries and companies to emit Greenhouse Gases (GHGs). One allowance is
equal to one tonne of Carbon Dioxide equivalent (CO 2 -eq). Annual reductions in the volume of
allowances available within the ETS are meant to gradually hinder contributions in emissions
from countries and companies.
  Historical data concludes with phase 3 of the ETS at the end of 2020. The timeseries for
projected forecasts of yearly emissions embodies phase 4 of the ETS (2021 – 2030).
Visualizations showcase emissions from EU Member States and EEA-EFTA states at the
country-level and sector-level. Three sectors dominate emission contributions within the ETS:
power and heat generation, energy-exhaustive industrial factories, and aviation. The aim of this
project is to quantify the influence of EU policy instruments on emissions vis-à-vis a cross-
sectoral comparison of allocation rate changes. Users can determine the rate of change for total
allocation of allowances per sector per country, generating a sense of autonomy in decision
making (like simulating the emergence of the Market Stability Reserve, for example).
  A business-as-usual model follows the EU’s quest towards carbon neutrality nearing 2030
through representation of current parameters set in place by phase 4 of the ETS. The guidelines
for free allocation of allowances have been modified to redirect attention towards high-risk
sectors prone to carbon leakage. Benchmark updates for annual reduction rates in freely allocated
allowances hinge on a sector’s innovation uptake. Sectors with lower innovation uptake will
receive a minimum annual reduction rate of 0.2%. Sectors with higher innovation uptake will
receive a maximum annual reduction rate of 1.6%. All allocations allotted for these sectors will
be free. Free allocation for less prone sectors will gradually phase out after 2026. The maximum
percentage of freely allocated allowances for less prone sectors will be 30%. By the end of phase
4 (2030), these less prone sectors will stop receiving free allocations.
  Our project is the creation of interactive, user-interface webtools that explore the relationship
between allowance allocations and CO 2 emissions under the EU ETS. Data is showcased based
on a user’s ideal set of parameterizations. Users can input any rate of change (%) in allowances
at the sector level for a given country and the model will adapt accordingly to show emission
changes. Total allocation is calculated through percentage decay from 2021 onwards (the end of
phase 3). If the allocation in 2021 is A, then in year 2021 + T, the allocation is Ar^{t}. We
allowed the rate of change in allowance reductions to range from 0 – 30%, a reasonable
bandwidth for reductions across the EU without shocking the market. This web tool is coupled
with an interactive dashboard of annual totals in CO 2 emission values (measured in million
tonnes) composed of EU Member States and EEA-EFTA state contributions up through phase 3
of the EU ETS (2005 – 2020).

## Introduction &amp; Background:
### EU ETS:

  The EU Emissions Trading System (ETS) is a “cap-and-trade” policy that allocates countries’
greenhouse gas (GHG) outputs by setting a threshold (cap) on the maximum amount of
emissions allowed within a given year. The countries participating under this system include the
EU Member States and EEA-EFTA states (Liechtenstein, Iceland, and Norway). This market-
based system incentivizes countries to purchase emission “allowances” that must be traded or
surrendered within a one-year timeframe. One allowance is equal to one tonne of Carbon
Dioxide equivalent (CO 2 -eq). Carbon pricing is influenced through this supply and demand
exchange between allowances. A reduction in GHG emissions is projected as the country-cap on
total emissions allowed is lowered. Countries that successfully reduce emissions can keep the
remaining “saved” allowances, either using them for future spending costs or selling them to
another entity in need of allowances.
  GHG emissions are assessed at the sector-level. Three broad sectors are governed under the EU
ETS – power and heat generation, energy-exhaustive industrial sectors, and aviation. These
sectors are the predominant emitters of the EU’s GHG total, accounting for roughly 41% of its
footprint. However, emission reductions upwards of 43% have been witnessed across these
sectors since the introduction of the EU ETS in 2005. In anticipation of a globally warming
future, the EU has amplified its net emission reduction goal to a minimum of 55% by 2030. To
reach this target, a sector-wide reduction of 61% is required (an additional 18% in emission
reductions compared to current sector-wide contributions).
### Reforms &amp; Future Implications:
  Several reforms have been presented to the ETS to reach the EU’s ambitious 2030 goal of a 55%
reduction in GHG emissions, using emissions recorded in 2005 as the baseline standard. Firstly,
annual emissions must be reduced by 4.2%. This can be achieved through a one-time “re-basing”
period that will cap overall emissions at 117 million allowances. In addition, the transition
towards full auctioning of allowances by 2027 has been suggested to stimulate higher carbon
pricing, which will catalyze a decline in overall emissions. A sector-specific approach will be
taken to reach the EU 2030 emissions target. Free allowances in the aviation sector will be
reduced gradually, and additional sectors will be considered in the trading market (starting with
the maritime transport sector).
### ETS Sectoral Emissions:
  The creation of a separate emissions trading system will account for reductions in targets not
included within the EU ETS – emissions stemming from fuels associated with road transport and
buildings, for instance. This newfound trading system places emphasis on fuel-based sector
emissions and is proposed to begin in 2025. An emissions cap will be determined based on
emissions recorded in the following year (2026). Fuel suppliers will assess the amount of fuels
they contributed within the market per year. Emission allowances surrendered will correspond to
the carbon intensity of a given fuel. Ultimately, the design of this new fuel-centric system
coerces fuel suppliers to decarbonize their products, effectively lowering compliance expenses
within the trading system.

  Aviation sector contributions toward emissions refers to flights within the European Economic
Area (EEA). Aviation emissions have been accounted for by the ETS since 2012 – with a vast
increase (5% yearly) in emissions recorded between 2013 and 2018. Reforms within the aviation
sector include accounting flights between UK and Switzerland, along with capping the total
concentration of allowances at current amounts. Total emission allowances will be reduced
yearly by 4.2%, including the number of free allowances allotted to aircraft operators. The goal
is to eliminate free allocation within the aviation sector altogether before 2027.
The aviation cap on emissions is determined through a set of rules that have remained constant in
phase 3 (2012 – 2020) and phase 4 (2021 – 2030) of the EU ETS. 82% of the total aviation cap is
composed of freely allocated allowances. 15% of allowances within the aviation cap are to be set
for auction. The remaining 3% of allowances are kept for the rare case of new entrants. In the
beginning of phase 4 (2021), the number of aviation allowances was roughly 24.5 billion. Based
on the rules set for the aviation cap, around 20.7 million allowances were freely allocated and
about 3.8 million were arranged for auction. From phase 3 onwards, a yearly linear reduction
factor of 2.2% will be applied to aviation allowances.
  Maritime transport sector contributions will also be considered to reach the future EU ETS goal
of a 55% reduction in emissions. Maritime transport refers to shipping, particularly the cargo-
capacity of a ship. All emissions from ships with a cargo-capacity above 5,000 gross tons
voyaging within the EU (intra-EU) will be accounted for. 50% of emissions from vessels with a
cargo-capacity above 5,000 gross tons voyaging beyond the EU (extra-EU) will also be
considered in the ETS. This proposal embodies nearly two-thirds of total EU maritime transport
emissions (90 million tonnes CO 2 ). Shipping companies will be placed as Member States, with
the responsibility of purchasing and surrendering emission allowances for each tonne of CO 2
released. This will ensure consistency in processing and comparing allowances across all sectors.
### Carbon Leakage &amp; Free Allowances:
  The allocation of free allowances will work to address a carbon leakage framework. Energy-
intensive sectors will be targeted for decarbonization efforts through the advancement of low-
carbon technologies. Carbon leakage under the EU ETS entails transferring sector emissions into
outside countries with different emission restrictions. Because the possibility of carbon leakage
is disproportionately expected within energy-intensive sectors, these highly prone industries will
receive a greater proportion of free allowances compared to their industrial counterparts.
Between 2013 and 2020 (phase 3 of the current trading period), nearly 60% of the EU ETS total
amounted allowances were auctioned. The remaining ~40% of allowances became available for
free apportionment. In the early phase of the trading period, most of these free allowances were
distributed among manufacturing sectors (80% of these industries allowances were freely
allocated). Yearly reductions in the quantity of free allowances distributed among manufacturing
industries dropped to 30% in 2020, but these sectors will continue receiving free allowances
beyond this timeframe. The aviation sector (airlines) currently receives the largest proportion of
free allowances. The surge in free allowances targeted at EU energy-exhaustive sectors is
expected to conclude in 2030.

### Benchmarks for Free Allowance Allocation:
  The allocation of free allowances has been determined through a benchmarking tactic since the
beginning of phase 3 (2013) of the EU ETS. Benchmarks are approached at the product-level and
are based on GHG estimates from the top performing 10% of installations for a particular
product. A total of 54 benchmarks comprises the EU ETS – one benchmark for each product.
This foundation of one product equating to one benchmark allows for consistency when
comparing the size, geographic location, or fuel spent on an installation. Installations are granted
full allowances to cover emissions when they reach these benchmarks. Likewise, installations
that do not reach these benchmarks are reprimanded with less allowances. These less efficient
installations are required to reduce emissions by purchasing additional allowances or credits.
A cross-sectoral correction factor was introduced at the beginning of phase 3 (2013) for instances
when installation allocations would surpass the proportion available for free allocation. This
correction factor reduced upwards of 11% of allocations in 2013. In essence, this correction
factor works inversely with allowances: an increase in the correction factor stimulates a decrease
in total allowance volume. The cross-sectoral correction factor reached a maximum of 22% in
2020, where it has remained.
  Allocation of free allowances for emerging installations in phase 4 are composed of two inputs:
the 200 million allowances pulled from the MSR, and the remaining un-allocated allowances that
were available for free allocation at the conclusion of phase 3 (2020). In addition, the 54
benchmark values that dictate the degree of free allocation for a given installation will be revised
during phase 4. These updates are meant to ensure levels of free allocation accurately mirror
levels of production. The minimum reduction rate of 0.2% targeted for sectors with more
complicated emission reduction avenues allows for guaranteed input. The maximum reduction
rate of 1.6% targeted for sectors of innovation kindles a sense of urgency to lower emissions at a
faster pace.

### Market Stability Reserve:
  The MSR serves to provide price stability over installations within the ETS carbon market. The
reserve offers flexibility for the EU ETS by rebalancing the supply and demand of carbon; it
reduces the new supply entering the market through auctions. This allows the market to be more
resilient to negative price impacts when demand is high, like during a global recession. A surplus
of allowances is expected during times of unforeseen economic crisis and amplified imports
through international credits. This excess in allowances drives the price of carbon down,
simultaneously abating the urgency to lower emissions.
  The MSR is a long-term strategy to compensate for the accumulation of allowances within the
EU ETS since 2009. The reserve came into effect in 2019 with 900 million “back-loaded”
allowances (garnered between the years 2014 through 2016). Threshold levels within the MSR
were set at a maximum of 833 million allowances, and minimum of 400 million allowances. At
the beginning of phase 3 (2013), roughly 2 billion allowances were accounted in surplus.
Through back-loading efforts, this surplus was reduced to approximately 1.78 billion allowances
by 2015.

  Back-loading of auctions are considered temporary, short-term solutions to the surplus of
allowances in the market (evident in 2019 with a postponed auctioning of 900 million allowances
that were instead back-loaded into the creation of the MSR). Back-loading of auction volumes
influences auction distributions by decreasing their occurrence during the phase 3 timeframe – it
does not, however, decrease the number of allowances set to be auctioned. A yearly decrease in
auction volume was seen between 2014 – 2016. The 900 million allowances back-loaded during
this period were transferred to stimulate the MSR in 2019.
  By design, the MSR influences the number of allowances in circulation (TNAC) through
accumulating or releasing parts of auction volumes. The 2015 MSR Decision fixed the intake
rate at 12% and capped the minimum number of allowances placed in the reserve to 100 million.
In 2019, this Decision was adjusted through a doubling scenario – the allowance intake rate
would double to 24% and the minimum number of allowances placed in the reserve would
double to 200 million. Essentially, when TNAC surpasses the upper threshold of 833 million,
24% of the allowances are removed through the MSR intake rate and placed into the reserve.
Likewise, if TNAC is less than the maximum lower threshold, 200 million allowances will be
released from the reserve and placed for auction. These doubled parameters would stay in effect
through 2023. After 2023, allowances contained within the MSR above the prior year’s auction
volume are nullified.
  Allowances in the reserve will be returned into the market if the estimated surplus reaches a
volume less than 400 million allowances. A monthly withdrawal rate of 1% from surplus
allowances (12% per annum) is analyzed and reviewed every September for the following year.
Unallocated phase 3 allowances were also funneled into the MSR, contributing a total estimated
amount around 550 to 700 million allowances.
### Annual Emissions Cap &amp; Stationary Installations:
  Market inequities are likewise reinforced through expedited measures that reduce yearly GHG
emissions. Yearly emission volumes are estimated through sectors (industry factories, power
plants, and aviation) and ‘capped’ based on a number of emission allowances. An allowance
grants an entity the jurisdiction to emit one tonne of a given GHG (CO 2 , N 2 O, or PFCs). During
phase 3 of the EU ETS (2013 – 2020), the cap on stationary installations was reduced yearly
through a linear reduction factor of 1.74%. The original cap for phase 3 (2013) was determined
by averaging the total amount of allowances given yearly within the timeframe of 2008 to 2012.
This capped emission rate will continue to decrease yearly into phase 4 of the EU ETS (2021 –
2030) through a linear reduction factor of 2.2%.
  In the beginning of phase 4 (2021), stationary installations were fixed at 1,571,583,007
allowances through a Union-wide cap. Yearly reductions in allowances are drive by the linear
reduction factor of 2.2%. This reduction equates to 43,003,515 allowances per year.
Three factors determine the level of free allocation for a given installation: benchmark estimates
capturing the averaged performance across the top 10% of best installations, the likelihood of
carbon leakage for a given sector, and historical activity levels. If the volume of allowances
available for free allocation exceeds calculated free allocations, a standard cross-sectoral
correction factor is applied. In hopes to avoid this cross-sectoral correction approach, a free
allocation buffer of sorts was created by reserving 3% of the total cap from auctioning (the 57%
auction share of allowances). If this allowance buffer of free allocations is not required, it is
distributed across varying funds (like the Innovation Fund and Modernisation Fund) at a set rate.
If free allocations remain after the fixed distribution across the listed funds, they are placed into
auction.

## Sources:
 https://www.eea.europa.eu/publications/the-eu-emissions-trading-system-2/the-eu-
emissions-trading-system
 https://ec.europa.eu/commission/presscorner/detail/en/qanda_21_3542
 https://climate.ec.europa.eu/eu-action/eu-emissions-trading-system-eu-ets/free-
allocation/allocation-industrial-installations_en
 https://climate.ec.europa.eu/eu-action/eu-emissions-trading-system-eu-ets/free-
allocation/carbon-leakage_en
 https://climate.ec.europa.eu/eu-action/eu-emissions-trading-system-eu-ets/free-
allocation_en
 https://climate.ec.europa.eu/eu-action/eu-emissions-trading-system-eu-ets/free-
allocation/allocation-aviation_en
 https://climate.ec.europa.eu/eu-action/eu-emissions-trading-system-eu-ets/free-
allocation/free-allocation-modernisation-energy-sector_en
 https://climate.ec.europa.eu/eu-action/eu-emissions-trading-system-eu-ets/market-
stability-reserve_en
 https://climate.ec.europa.eu/eu-action/climate-strategies-targets/2030-climate-energy-
framework_en
 https://climate.ec.europa.eu/eu-action/eu-emissions-trading-system-eu-ets/emissions-cap-
and-allowances_en
 https://climate.ec.europa.eu/eu-action/eu-emissions-trading-system-eu-ets/free-
allocation_en#free-allocation-decreases-each-year
 https://climate.ec.europa.eu/news-your-voice/news/further-information-start-phase-4-eu-
ets-2021-emission-allowances-be-issued-aircraft-operators-and-2020-12-11_en
 https://redshawadvisors.com/learn-carbon/eu-ets/market-stability-
reserve/#:~:text=The%20Market%20Stability%20Reserve%20(MSR,green%20technology%
20and%20energy%20efficiency
 https://euets.info/static/download/Description_EUTL_database.pdf
Data Download:
 https://euets.info/download/
 https://www.eea.europa.eu/data-and-maps/data/european-union-emissions-trading-
scheme-17
