[EN]
## V1
V1: Linear Thermal Approximation & Percolation ThresholdThis initial analytical model focuses on calculating the electrical percolation threshold ($\Phi_c$) of Ag2Se nanowires within a PEDOT:PSS polymer matrix. 

While it successfully simulates the power-law spike in electrical conductivity post-percolation, 
it utilizes a simplified linear mixing rule for thermal conductivity. By excluding the electronic thermal conductivity component (Wiedemann-Franz effect), 
**this version predicts an artificially high ZT at large volume fractions.** It serves as a foundational baseline for understanding the core electrical mechanism.

### Key Physics Addressed:
* **Percolation Theory:** Simulating the critical threshold ($\Phi_c$) where nanowires form a continuous conductive network inside the insulating/semi-conducting polymer matrix.
* **Power Law Conductivity:** Utilizing the universal scaling law for 3D networks to calculate electrical conductivity post-percolation.
* **Thermoelectric Efficiency:** Calculating the resulting $ZT$ value at room temperature (300K) using the Seebeck coefficient, electrical conductivity, and thermal conductivity mix.

### 🛠️ Upcoming Phases
- Implementing non-linear thermal conductivity spikes post-percolation.
- Exporting optimized material parameters to **COMSOL Multiphysics** for Heat Transfer and multiphysics modeling of cylindrical geometries.

## V2
V2: Wiedemann-Franz Correction

Building upon V1, this iteration incorporates the dual nature of thermal transport in semiconductors: both phonon (lattice) and electron contributions. By applying the Wiedemann-Franz law using the Lorenz number, the model now accurately reflects the simultaneous spike in electronic thermal conductivity alongside electrical conductivity. This crucial correction reveals the realistic "sweet spot" (peak ZT) on the curve, allowing us to identify the optimal filler ratio for flexible thermoelectric composites at industrial standards.

## 🛑 Analytical Limitations and Transition to FEA
These Python-based analytical models successfully calculate electrical conductivity and percolation mechanisms assuming a flawless 1D matrix. However, real-world polymer-metal composites exhibit 3D agglomeration and high interface resistance at larger volume fractions (typically >20%). 

Because pure analytical mathematics cannot account for these physical defects, the current model does not fully capture the expected drop in the ZT curve at high concentrations. To overcome this limitation and accurately model the 3D thermal mapping of flexible bands wrapped around heat pipes, the next phase of this research will transition into Finite Element Analysis (FEA) using **COMSOL Multiphysics**.

------------------------------------------------------------------------------------------
[TR]

## V1
V1: Doğrusal Termal Yaklaşım ve Sızma Eşiği (Linear Thermal Approximation & Percolation Threshold)Bu ilk analitik model, PEDOT:PSS polimer matrisi içindeki Ag2Se nanotellerinin elektriksel sızma eşiğini (percolation threshold - $\Phi_c$) hesaplamaya odaklanmaktadır.

Model, hacim kesri arttıkça elektriksel iletkenlikteki üstel (power-law) artışı başarılı bir şekilde simüle ederken, termal iletkenliği basitleştirilmiş bir doğrusal karışım kuralı ile ele almaktadır. Elektronik termal iletkenliğin (Wiedemann-Franz etkisi) göz ardı edilmesi nedeniyle, bu versiyon yüksek hacim kesirlerinde teorik sınırların ötesinde bir ZT değeri öngörmektedir. Temel mekanizmayı anlamak için oluşturulmuş bir referans noktasıdır.

### Ele Alınan Temel Fizik:
* **Süzme Teorisi:** Nanotellerin yalıtkan/yarı iletken polimer matris içinde sürekli bir iletken ağ oluşturduğu kritik eşiğin ($\Phi_c$) simüle edilmesi.
* **Güç Yasası İletkenliği:** Süzme sonrası elektriksel iletkenliği hesaplamak için 3D ağlar için evrensel ölçeklendirme yasasını kullanma.
* **Termoelektrik Verimlilik:** Oda sıcaklığında (300K) elde edilen $ZT$ değerinin Seebeck katsayısı, elektriksel iletkenlik ve termal iletkenlik karışımı kullanılarak hesaplanması.

### 🛠️ Yaklaşan Aşamalar
- Süzme sonrasında doğrusal olmayan termal iletkenlik artışlarının uygulanması.
- Isı Transferi ve silindirik geometrilerin çoklu fizik modellemesi için optimize edilmiş malzeme parametrelerinin **COMSOL Multiphysics**'e aktarılması.

## V2
V2: Wiedemann-Franz Düzeltmesi (Wiedemann-Franz Correction)

V1 modelindeki analitik eksiklikler giderilerek, ısıl iletimin hem fonon (örgü) hem de elektron taşıyıcıları tarafından gerçekleştirildiği gerçeği V2 modeline entegre edilmiştir. Lorenz numarası kullanılarak Wiedemann-Franz yasası koda dahil edilmiş; böylece Ag2Se eklendikçe elektriksel iletkenlikle beraber elektronik termal iletkenliğin de eşzamanlı arttığı bir sistem modellenmiştir. Bu düzeltme, ZT eğrisindeki gerçekçi "tepe noktasını" (sweet spot) ortaya çıkarmış ve esnek termoelektrik kompozitler için optimum dolgu oranını endüstriyel standartlarda tespit etmemizi sağlamıştır.

## 🛑 Analitik Sınırlar ve Sonlu Elemanlar Analizine (FEA) Geçiş

Python tabanlı bu analitik modeller, elektriksel iletkenlik ve sızma eşiği mekanizmalarını 1 boyutlu (1D) kusursuz bir matris üzerinden başarıyla hesaplamıştır. Ancak, gerçek dünyadaki polimer-metal kompozitler yüksek dolgu oranlarında (%20 ve üzeri) 3 boyutlu topaklanma (agglomeration) ve yüksek arayüzey direnci (interface resistance) sergiler. 

Kusursuz matematiğin bu fiziksel kusurları (defect) hesaba katamaması nedeniyle, model belli bir hacim kesrinden sonra ZT eğrisinde beklenen düşüşü gösterememiştir. Bu sınırlamayı aşmak ve sıcaklık boruları etrafına sarılan gerçek esnek bantların 3 boyutlu termal haritalarını çıkarabilmek için, araştırmanın bir sonraki fazı **COMSOL Multiphysics** kullanılarak Sonlu Elemanlar Analizi (FEA) ortamına taşınacaktır.
