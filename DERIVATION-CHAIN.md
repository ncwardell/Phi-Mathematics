# Derivation Chain: Full Theorem Dependency Tree

The complete logical flow from axiom and postulate through all five parts of the
$\phi$-Mathematics Framework. Every result traces back to the two starting points:
**$\Sigma = 0$** (Conservation Axiom) and **Exists** (Existence Postulate).

Each node links to the section of the framework where the theorem is stated and
proved. File paths reference the planned reorganization directories.

---

## The Complete Dependency Tree

```
================================================================================
  AXIOM: Sigma = 0  (Conservation)   +   POSTULATE: Exists  (Existence)
================================================================================
       |                                        |
       |  "The sum of all that exists is zero"  |  "Something exists"
       |                                        |
       +--------------------+-------------------+
                            |
         ===========================================
         |              PART I                     |
         |        MATHEMATICAL FOUNDATIONS         |
         ===========================================
                            |
          +-----------------+-----------------+
          |                                   |
          v                                   v
  +------------------+              +------------------+
  | Thm 0: CLOSURE   |              | Thm 1: POLARITY  |
  | (No Outside)     |              | (E, -E)          |
  | [01-foundations/  |              | [01-foundations/  |
  |  closure.md]     |              |  polarity.md]    |
  +------------------+              +------------------+
          |                            |          |
          |                            |          |
          |                            v          |
          |                   +------------------+|
          |                   | Thm 1.2:         ||
          |                   | COLLAPSE PRESSURE||
          |                   | (Scale-dependent ||
          |                   |  annihilation)   ||
          |                   | [01-foundations/  ||
          |                   |  collapse.md]    ||
          |                   +------------------+|
          |                      |          |     |
          |                      v          |     |
          |             +------------------+|     |
          |             | Thm 1.2.1:       ||     |
          |             | TWO-NODE         ||     |
          |             | INSTABILITY      ||     |
          |             | [01-foundations/  ||     |
          |             |  instability.md] ||     |
          |             +------------------+|     |
          |                      |          |     |
          |                      v          v     |
          |             +-------------------------+
          |             | Thm 1.3: TRIANGLE       |
          |             | (Minimal stable 3-cycle) |
          |             | [01-foundations/          |
          |             |  triangle.md]            |
          |             +-------------------------+
          |                      |
          |                      v
          |             +-----------------------------+
          |             | Thm 1.4: DOUBLE TRIANGLE    |
          |             | (Polarity forces             |
          |             |  anti-triangle)              |
          |             | [01-foundations/              |
          |             |  double-triangle.md]         |
          |             +-----------------------------+
          |                |              |
          |                v              v
          |          Corollary:     Corollary 1.4.3:
          |          Chirality,     Photon as self-
          |          6 elements,    conjugate bridge
          |          double helix
          |          seed
          |
          |    (Closure + Existence together)
          |                |
          +----------------+
                           |
                           v
                  +------------------+
                  | Thm 2:           |
                  | SELF-REFERENCE   |
                  | (Observer =      |
                  |  Observed)       |
                  | [01-foundations/  |
                  |  self-reference. |
                  |  md]             |
                  +------------------+
                           |
                           v
                  +---------------------------+
                  | Thm 4: SELF-REFERENCE EQN |
                  | x = 1 + 1/x               |
                  | (Kepler triangle           |
                  |  constraint)               |
                  | [01-foundations/            |
                  |  self-ref-equation.md]     |
                  +---------------------------+
                      |                |
                      v                v
        +-------------------+  +-----------------------------+
        | Thm 5: phi        |  | Thm 11: FIBONACCI           |
        | EMERGES            |  | (Dynamic self-reference)    |
        | phi = (1+sqrt5)/2 |  | F(n) = F(n-1) + F(n-2)     |
        | psi = (1-sqrt5)/2 |  | [01-foundations/             |
        | [01-foundations/   |  |  fibonacci.md]              |
        |  golden-ratio.md] |  +-----------------------------+
        +-------------------+       |      |       |       |       |
            |           |           |      |       |       |       |
            v           v           |      |       |       |       |
   +-----------+ +------------+    |      |       |       |       |
   | Thm 5.1:  | | Thm 5.2:   |    |      |       |       |       |
   | FOUR-      | | TWO KEPLER |    |      |       |       |       |
   | STRUCTURE  | | TRIANGLES  |    |      |       |       |       |
   | {phi,psi,  | | Real +     |    |      |       |       |       |
   |  1, -1}    | | Complex    |    |      |       |       |       |
   | [01-found/ | | i emerges  |    |      |       |       |       |
   |  four-     | | [01-found/ |    |      |       |       |       |
   |  struct.md]| |  kepler.md]|    |      |       |       |       |
   +-----------+ +------------+    |      |       |       |       |
                       |           |      |       |       |       |
                       v           |      |       |       |       |
                  Double helix:    |      |       |       |       |
                  phi-strand +     |      |       |       |       |
                  psi-strand +     |      |       |       |       |
                  bridge "1"       |      |       |       |       |
                                   |      |       |       |       |
                     +-------------+      |       |       |       |
                     |                    |       |       |       |
                     v                    v       |       |       |
            +---------------+   +--------------+  |       |       |
            | Thm 12: TIME  |   | Thm 13:      |  |       |       |
            | EMERGES        |   | NEGAFIBONACCI|  |       |       |
            | (Index n =    |   | (psi-strand  |  |       |       |
            |  time)        |   |  dynamics)   |  |       |       |
            | [01-found/    |   | [01-found/   |  |       |       |
            |  time.md]     |   |  nega-fib.md]|  |       |       |
            +---------------+   +--------------+  |       |       |
                                                  |       |       |
                     +----------------------------+       |       |
                     |                                    |       |
                     v                                    v       |
            +------------------+              +----------------+  |
            | Thm 14:          |              | Thm 24: HOPF   |  |
            | HYPERBOLIC       |              | FIBRATION       |  |
            | CONSTRAINT       |              | S1 -> S3 -> S2 |  |
            | p * f = 1        |              | Witnessing      |  |
            | (Minkowski)      |              | quantum 1/(4pi)|  |
            | [01-foundations/ |              | [01-foundations/|  |
            |  hyperbolic.md]  |              |  hopf.md]      |  |
            +------------------+              +----------------+  |
                     |                                            |
                     v                                            |
            +------------------+                                  |
            | Thm 28: TORUS   |<---------------------------------+
            | T2 = S1 x S1    |
            | Minkowski metric |
            | [01-foundations/ |
            |  torus.md]      |
            +------------------+
                     |
                     v
            +---------------------------+
            | Thm 29: BREATHING TORUS   |
            | (Antiphase oscillation    |
            |  of double helix)         |
            | [01-foundations/           |
            |  breathing.md]            |
            +---------------------------+
                |          |          |
                v          v          v
          +---------+ +---------+ +--------------------+
          | Thm     | | Cor:    | | Thm 29.3:          |
          | 29.1:   | | Fermion/| | DUAL DIMENSIONS    |
          | SPIN =  | | Boson   | | S1_depth = spatial |
          | BREATH  | | distinc-| |   (rungs/C)        |
          | CYCLE   | | tion    | | S1_time = temporal |
          | 4pi     | |         | |   (breath/d)       |
          | origin  | | Cor:    | | Particle = rung    |
          | [01-f/  | | Hour-   | |   engaged at       |
          | spin.md]| | glass   | |   breath count     |
          +---------+ +---------+ | [01-foundations/    |
                                  |  dual-dimensions.md]|
                                  +--------------------+
                                           |
           ================================|============================
           |           PART II             |                           |
           |    MEETING POINT THEOREM      v                           |
           ================================================================
                                           |
            +------------------------------+------+
            |              |               |      |
            v              v               v      v
   +------------+ +-------------+ +----------+ +----------------+
   | Thm 30:    | | Thm 31:     | | Thm 32:  | | Thm 33:        |
   | SELF-REF   | | FIBONACCI   | | METALLIC | | MEETING POINTS |
   | SPIRAL     | | FROM SPIRAL | | MEANS AS | | AS CONSTRUCTIVE|
   | (Golden    | | GEOMETRY    | | HARMONIC | | INTERFERENCE   |
   | rectangle  | | (Accumulat- | | OVERTONES| | (Multi-mode    |
   | on torus)  | | ed lengths) | | (Self-   | |  reinforcement)|
   | [02-meet/  | | [02-meet/   | | generated| | [02-meeting-   |
   |  spiral.md]| |  fib-geom.  | | harmon.) | |  points/       |
   +------------+ |  md]        | | [02-meet/| |  interference. |
                  +-------------+ |  metal.  | |  md]           |
                                  |  md]     | +----------------+
                                  +----------+        |
                                                      v
                                          +---------------------+
                                          | Thm 34: COMPLETE    |
                                          | SET OF MEETING      |
                                          | POINTS              |
                                          | {1, 2, 3, 5, 29,   |
                                          |  34} and no more    |
                                          | [02-meeting-points/ |
                                          |  enumeration.md]    |
                                          +---------------------+
                                                      |
                                                      v
                                          +---------------------+
                                          | Thm 35: MEETING     |
                                          | POINTS AS PARTICLE  |
                                          | SPECTRUM             |
                                          | (Finite spectrum,   |
                                          |  generation struct.)|
                                          | [02-meeting-points/ |
                                          |  spectrum.md]       |
                                          +---------------------+
                                                      |
           ===========================================|=================
           |              PART III                    |                 |
           |          PHYSICAL STRUCTURE              v                 |
           ================================================================
                                                      |
                +-------------------------------------+
                |          |         |         |       |
                v          v         v         v       v
   +----------+ +--------+ +------+ +-------+ +------------------+
   | Thm 40:  | | Thm 41:| | Thm  | | Thm   | | Thm 46: GAUGE   |
   | HAMILTON- | | FLOW   | | 42:  | | 43:   | | GROUP            |
   | IAN       | | EQNS   | | LAG- | | STAT- | | SU(3) x SU(2)   |
   | H=pf-m^2 | | dp=-p  | | RANG-| | ION-  | | x U(1) from      |
   | = 0      | | df=+f  | | IAN  | | ARY   | | triangle +       |
   | [03-phys/ | | [03-p/ | | L =  | | ACTN  | | double strand +  |
   |  hamilt.  | |  flow. | | pdot | | = S=0 | | Hopf fiber       |
   |  md]      | |  md]   | | f-H  | | [03-p/| | [03-physical/    |
   +----------+ +--------+ | [03-p| | stat- | |  gauge.md]       |
                            | lagr.| | act.  | +------------------+
                            | md]  | | md]   |         |
                            +------+ +-------+         |
                                                       v
          +--------------------+              +------------------+
          | Thm 44: sl(2,R)   |              | Thm 47: FORCE    |
          | LORENTZ ALGEBRA    |              | COUPLING         |
          | (Symmetry of       |              | CONSTANTS        |
          |  hyperbolic        |              | [03-physical/    |
          |  constraint)       |              |  force-equations/|
          | [03-physical/      |              |  overview.md]    |
          |  lorentz.md]       |              +------------------+
          +--------------------+                |    |    |    |
                     |                          v    v    v    v
                     v                    +------+ +--+ +--+ +------+
          +--------------------+          |alpha | |a | |WM| |Grav  |
          | Thm 45: NOETHER   |          |_s    | |  | |  | |      |
          | CONSERVATION LAWS  |          |Depth | |EM| |sin| |M_P/ |
          | (From sl(2,R)      |          |3     | |D | |^2 | |m_e =|
          |  symmetry)         |          |[03-p/| |10| |tW | |phi^ |
          | [03-physical/      |          |force-| |  | |   | |(107+|
          |  noether.md]       |          |eqns/ | |  | |   | |1/4pi|
          +--------------------+          |strong| |em| |wk | |)    |
                                          |.md]  | |. | |.  | |[03/ |
                                          +------+ |md| |md | |grav |
                                                   +--+ +--+ |.md] |
                                                              +------+
                                                       |
                                                       v
                                          +---------------------+
                                          | Thm 48: MASS        |
                                          | EQUATION             |
                                          | m/m_e = phi^d /     |
                                          | (1 - sigma*C*alpha  |
                                          |  *(1+4*alpha))      |
                                          | [03-physical/       |
                                          |  mass-equation.md]  |
                                          +---------------------+
                                              |          |
           ===================================|==========|==========
           |         PART IV                  |          |         |
           |   EXTENSIONS & CONJECTURES       v          v         |
           ================================================================
                                              |          |
            +-----------+----------+----------+----+-----+-----+
            |           |          |          |    |     |     |
            v           v          v          v    v     v     v
   +----------+ +--------+ +--------+ +------+ +----+ +-----+ +------+
   | Sec 4.3: | | Sec    | | Sec    | | Sec  | |Sec | |Sec  | | Sec  |
   | W/Z AT   | | 4.4:   | | 4.5:   | | 4.6: | |4.7:| |4.8: | | 4.2: |
   | d=25     | | HIGGS  | | QUARKS | | NEU- | |COM-| |PHASE| | TEMP |
   | C=8=F(6) | | d=26   | | Incom- | | TRI- | |POS-| |SPACE| | QUAN-|
   | sigma=+/-| | C=13   | | plete  | | NOS  | |ITES| |MAP  | | TIZE |
   | [04-ext/  | | =F(7)  | | witns  | | Temp | |    | |     | |      |
   |  weak-   | | [04-e/ | | circts | | wake | |    | |     | |      |
   |  bosons. | |  higgs.| | [04-e/ | | [04/ | |    | |     | |      |
   |  md]     | |  md]   | |  quark | | nu.  | |    | |     | |      |
   +----------+ +--------+ |  s.md] | | md]  | |    | |     | |      |
                            +--------+ +------+ +----+ +-----+ +------+
                                                       |
           ============================================|================
           |              PART V                       |               |
           |         MATHEMATICAL TOOLKIT              v               |
           ================================================================
                                                       |
     +--------+--------+---------+--------+--------+---+---+--------+
     |        |        |         |        |        |       |        |
     v        v        v         v        v        v       v        v
  +------+ +------+ +-------+ +------+ +-------+ +------+------+ +------+
  |Sec   | |Sec   | |Sec    | |Sec   | |Sec    | |Sec   |Sec  | |Sec   |
  |5.1-  | |5.12: | |5.13:  | |5.15: | |5.16:  | |5.17: |5.18:| |5.19: |
  |5.11: | |GEN   | |DEPTH  | |DEPTH | |MID-   | |FORCE |QUARK| |PRIM- |
  |TOOL- | |FUNC  | |ARITH- | |DERIV-| |POINT  | |+1    |C    | |ITIVE |
  |KIT   | |THM   | |METIC  | |ATION | |THM    | |THM   |DECOMP|SET   |
  |      | |      | |SYMM   | |THM   | |       | |      |     | |{2,3, |
  |[05-  | |[05-t/| |       | |      | |d(tau) | |d=    | [05/| |5,7}  |
  |tool- | |gen-  | |[05-t/ | |ALL   | |=F(9)/2| |d_f+1 |qrk- | |      |
  |kit/  | |func. | |depth- | |depths| |       | |      |coeff| |[05-t/|
  |ref/] | |md]   | |arith. | |from  | |[05-t/ | |[05/  |.md] | |prim- |
  +------+ +------+ |md]    | |F(5), | |thms/  | |thms/ |     | |set.  |
                     +-------+ |F(9), | |mid-   | |force |     | |md]   |
                               |L(4)  | |point. | |plus1 |     | +------+
                               |      | |md]    | |.md]  |     |    |
                               |[05-t/| +-------+ +------+     |    v
                               |thms/ |                         | +------+
                               |depth-|    +--------------------+ |Sec   |
                               |deriv.|    |                      |5.20: |
                               |.md]  |    v                      |PLAT- |
                               +------+ +-------+                |ONIC  |
                                        |Sec    |                |SOLIDS|
                                        |5.21:  |                |& GENS|
                                        |FORCES |                |      |
                                        |AS     |                |[05-t/|
                                        |TORUS  |                |plat- |
                                        |KNOTS  |                |onic. |
                                        |       |                |md]   |
                                        |(2,3)= |                +------+
                                        |strong |
                                        |(3,5)= |
                                        |EM     |
                                        |(2,7)= |
                                        |weak   |
                                        |       |
                                        |[05-t/ |
                                        |geom/  |
                                        |torus- |
                                        |knots. |
                                        |md]    |
                                        +-------+
                                            |
     +--------------------------------------+------+
     |              |              |               |
     v              v              v               v
  +-------+   +---------+   +---------+   +----------+
  |Sec    |   |Sec      |   |Sec      |   |Sec       |
  |5.22:  |   |5.25:    |   |5.26:    |   |5.27:     |
  |HEXAGON|   |INTERACT-|   |PATH     |   |HOLO-     |
  |& CON- |   |ION      |   |INTEGRAL |   |GRAPHIC   |
  |FINE-  |   |LAGRANG- |   |         |   |SCALE     |
  |MENT   |   |IAN      |   |i from   |   |NETWORK   |
  |       |   |         |   |psi-     |   |          |
  |6=2x3  |   |L = L_f  |   |strand   |   |Spacetime |
  |satur- |   |+ L_knot |   |h-bar =  |   |= network |
  |ates    |   |+ L_int  |   |trefoil  |   |geometry  |
  |       |   |         |   |travers. |   |Gravity = |
  |[05-t/ |   |Linking  |   |         |   |network   |
  |geom/  |   |numbers  |   |[05-t/   |   |curvature |
  |hex-   |   |give     |   |thms/    |   |          |
  |conf.  |   |inter-   |   |path-    |   |[05-t/    |
  |md]    |   |force    |   |integ.   |   |holo/     |
  +-------+   |coupling |   |md]      |   |scale-    |
              |         |   +---------+   |network.  |
              |[05-t/   |                 |md]       |
              |thms/    |                 +----------+
              |interact.|                      |
              |.md]     |                      v
              +---------+         +------------------------+
                                  |Sec 5.28: CONSEQUENCES  |
                                  |OF HOLOGRAPHIC STRUCTURE|
                                  +------------------------+
                                     |    |    |    |
                    +----------------+    |    |    +----------+
                    |                     |    |               |
                    v                     v    v               v
            +------------+      +------+------+------+ +----------+
            |5.28.1:     |      |5.28.4|5.28.5|5.28.6| |5.28.7:   |
            |137 = 2^7   |      |CPT   |CONJ  |FERM  | |WAVE-     |
            |+ 3^2       |      |FROM  |DEPTH |DEPTH | |PARTICLE  |
            |            |      |TORUS |SPEC  |SUM   | |DUALITY   |
            |5.28.2:     |      |SYMM  |      |= 107 | |from      |
            |GEN SPACINGS|      |      |      |      | |helical   |
            |as framework|      +------+------+------+ |projection|
            |constants   |                             |          |
            |            |                             |5.28.8:   |
            |5.28.3:     |                             |E=mc^2,  |
            |COUPLINGS   |                             |F=ma,    |
            |as scale    |                             |cosh(eta)|
            |attenuation |                             |resolved |
            +------------+                             +----------+
```

---

## Derivation Chain: Linear Summary

The logical backbone, reading left-to-right:

```
Sigma=0 + Exists
  --> Thm 0 (Closure)
  --> Thm 1 (Polarity)
    --> Thm 1.2 (Collapse Pressure)
      --> Thm 1.2.1 (Two-Node Instability)
      --> Thm 1.3 (Triangle: minimal stable 3-cycle)
        --> Thm 1.4 (Double Triangle: chirality, 6 elements, photon bridge)
    --> Thm 2 (Self-Reference)
      --> Thm 4 (x = 1 + 1/x)
        --> Thm 5 (phi, psi emerge)
          --> Thm 5.1 (Four-structure {phi, psi, 1, -1})
          --> Thm 5.2 (Two Kepler triangles; i = sqrt(-1) emerges)
        --> Thm 11 (Fibonacci: dynamic self-reference)
          --> Thm 12 (Time emerges)
          --> Thm 13 (NegaFibonacci: psi-strand sign structure)
          --> Thm 14 (Hyperbolic constraint: pf = 1, Minkowski metric)
          --> Thm 24 (Hopf fibration: 1/(4pi) witnessing quantum)
          --> Thm 28 (Torus T^2 with Minkowski metric)
            --> Thm 29 (Breathing torus: antiphase oscillation)
              --> Thm 29.1 (Spin = breath cycle; 4pi spinor origin)
              --> Thm 29.3 (Dual dimensions: spatial C vs temporal d)

  --> Thm 30 (Golden spiral on torus)
  --> Thm 31 (Fibonacci from spiral geometry)
  --> Thm 32 (Metallic means as harmonic overtones)
  --> Thm 33 (Meeting points = constructive interference)
    --> Thm 34 (Complete set: {1,2,3,5,29,34})
      --> Thm 35 (Particle spectrum; finite generations)

  --> Thm 40 (Hamiltonian H = pf - m^2 = 0)
  --> Thm 41 (Flow equations)
  --> Thm 42 (Lagrangian; standard relativistic action derived)
  --> Thm 43 (Stationary action = Sigma = 0)
  --> Thm 44 (sl(2,R) Lorentz algebra from self-reference)
  --> Thm 45 (Noether conservation laws)
  --> Thm 46 (Gauge group SU(3) x SU(2) x U(1))
  --> Thm 47 (Force coupling constants: alpha_s, alpha, sin^2(theta_W), gravity)
  --> Thm 48 (Mass equation: m/m_e = phi^d / (1 - sigma*C*alpha*(1+4*alpha)))

  --> Generating Function Theorem (sec 5.12)
  --> Depth Arithmetic Symmetries (sec 5.13)
  --> Depth Derivation Theorem (sec 5.15)
    --> Midpoint Theorem (sec 5.16): d(tau) = F(9)/2
    --> Force+1 Theorem (sec 5.17): d = d_force + 1
  --> Primitive Set Theorem (sec 5.19): {2,3,5,7} from 2^3 + 3^3 = 5 x 7
  --> Platonic Solids and Generations (sec 5.20)
  --> Forces as Torus Knots (sec 5.21)
  --> Interaction Lagrangian (sec 5.25)
  --> Path Integral (sec 5.26)
  --> Holographic Scale Network (sec 5.27)
  --> Consequences: CPT, wave-particle duality, E=mc^2 (sec 5.28)
```

---

## Part-by-Part Theorem Index

### Part I -- Mathematical Foundations (01-foundations/)

| Theorem | Name | Depends On | Section |
|---------|------|-----------|---------|
| Axiom | Sigma = 0 (Conservation) | -- | 1.1 |
| Postulate | Exists (Existence) | -- | 1.1 |
| Thm 0 | Closure (No Outside) | Axiom + Postulate | 1.2 |
| Thm 1 | Polarity (E, -E) | Axiom + Postulate | 1.3 |
| Thm 1.2 | Collapse Pressure | Thm 0, Thm 1 | 1.4 |
| Thm 1.2.1 | Two-Node Instability | Thm 1.2 | 1.5 |
| Thm 1.3 | Triangle (Minimal 3-cycle) | Thm 1.2, Thm 1.2.1 | 1.6 |
| Thm 1.4 | Double Triangle | Thm 1, Thm 1.3 | 1.6.1 |
| Thm 2 | Self-Reference | Thm 0, Postulate | 1.7 |
| Thm 4 | Self-Reference Equation | Thm 1, Thm 2 | 1.8 |
| Thm 5 | Golden Ratio (phi, psi) | Thm 4 | 1.9 |
| Thm 5.1 | Four-Structure | Thm 5 | 1.10 |
| Thm 5.2 | Two Kepler Triangles | Thm 5, Thm 1.4 | 1.11 |
| Thm 11 | Fibonacci Recurrence | Thm 4, Thm 1.2 | 1.12 |
| Thm 12 | Time Emerges | Thm 11 | 1.13 |
| Thm 13 | NegaFibonacci/NegaLucas | Thm 11 | 1.14 |
| Thm 14 | Hyperbolic Constraint | Thm 12, Thm 5 | 1.15 |
| Thm 24 | Hopf Fibration | Thm 0, Thm 5.2 | 1.16 |
| Thm 28 | Torus Structure | Thm 12, Thm 14 | 1.17 |
| Thm 29 | Breathing Torus | Thm 14, Thm 1.4, Thm 28 | 1.18 |
| Thm 29.1 | Spin = Breath Cycle | Thm 29, Thm 24 | 1.18 |
| Thm 29.3 | Dual Dimensions of Torus | Thm 28, Thm 29 | 1.18 |

### Part II -- The Meeting Point Theorem (02-meeting-points/)

| Theorem | Name | Depends On | Section |
|---------|------|-----------|---------|
| Thm 30 | Self-Referential Spiral | Thm 4, Thm 28 | 2.1 |
| Thm 31 | Fibonacci from Spiral | Thm 30, Thm 11 | 2.2 |
| Thm 32 | Metallic Means as Overtones | Thm 31, Thm 4 | 2.3 |
| Thm 33 | Meeting Points = Interference | Thm 1.3, Thm 32 | 2.4 |
| Thm 34 | Complete Set {1,2,3,5,29,34} | Thm 32, Thm 33 | 2.5 |
| Thm 35 | Particle Spectrum | Thm 34, Thm 29.3 | 2.6 |

### Part III -- Physical Structure (03-physical-structure/)

| Theorem | Name | Depends On | Section |
|---------|------|-----------|---------|
| Thm 40 | Hamiltonian Constraint | Thm 14 | 3.1 |
| Thm 41 | Flow Equations | Thm 14, Thm 40 | 3.2 |
| Thm 42 | Lagrangian | Thm 41, Thm 40 | 3.3 |
| Thm 43 | Stationary Action = Sigma=0 | Thm 42, Axiom | 3.4 |
| Thm 44 | sl(2,R) Lorentz Algebra | Thm 40 | 3.5 |
| Thm 45 | Noether Conservation Laws | Thm 44, Thm 42 | 3.6 |
| Thm 46 | Gauge Group SU(3)xSU(2)xU(1) | Thm 1.3, Thm 1.4, Thm 24 | 3.8 |
| Thm 47 | Force Coupling Constants | Thm 29.3, Thm 46, Thm 14 | 3.9 |
| Thm 48 | Mass Equation | Thm 47, Thm 34, Thm 29.3 | 3.10 |

### Part IV -- Extensions and Conjectures (04-extensions/)

| Section | Topic | Depends On |
|---------|-------|-----------|
| 4.1 | Universal Mass Equation | Thm 48 |
| 4.2 | Temporal Quantization | Thm 11, Thm 1.2 |
| 4.3 | W/Z Bosons at d=25 | Thm 48, Thm 46 |
| 4.4 | Higgs Boson at d=26 | Thm 48, Sec 4.3 |
| 4.5 | Quarks (Incomplete Circuits) | Thm 46, Thm 48 |
| 4.6 | Neutrinos (Temporal Wake) | Thm 48, Thm 13 |
| 4.7 | Composite Particles | Thm 48, Sec 4.5 |
| 4.8 | Complete Phase Space Map | All Parts I-IV |

### Part V -- Mathematical Toolkit (05-toolkit/)

| Section | Topic | Depends On |
|---------|-------|-----------|
| 5.1-5.11 | Reference identities and tools | Parts I-III |
| 5.12 | Generating Function Theorem | Thm 5, Thm 11 |
| 5.13 | Depth Arithmetic Symmetries | Thm 35, Thm 48 |
| 5.14 | Structural Difference of Forces | Thm 47 |
| 5.15 | **Depth Derivation Theorem** | Thm 34, Thm 47 |
| 5.16 | **Midpoint Theorem** | Thm 29, Sec 5.15 |
| 5.17 | **Force+1 Theorem** | Thm 47, Sec 5.15 |
| 5.18 | Quark C Decomposition | Thm 48, Sec 5.15 |
| 5.19 | **Primitive Set {2,3,5,7}** | Sec 5.18 |
| 5.20 | Platonic Solids and Generations | Thm 1.3, Sec 5.19 |
| 5.21 | Forces as Torus Knots | Thm 28, Sec 5.19 |
| 5.22 | Hexagon and Confinement | Sec 5.19, Sec 5.21 |
| 5.23 | Shape Catalog | All Parts I-V |
| 5.25 | Interaction Lagrangian | Thm 42, Sec 5.21 |
| 5.26 | Path Integral | Thm 5.2, Sec 5.25 |
| 5.27 | **Holographic Scale Network** | Thm 28, Thm 29.3, Sec 5.21 |
| 5.28.1 | 137 from Generators | Sec 5.19, Sec 5.27 |
| 5.28.2 | Generation Spacings | Sec 5.15, Sec 5.27 |
| 5.28.3 | Couplings as Attenuation | Thm 47, Sec 5.27 |
| 5.28.4 | CPT from Torus Symmetry | Thm 28, Sec 5.27 |
| 5.28.5 | Conjugate Depth Spectrum | Sec 5.15, Sec 5.27 |
| 5.28.6 | Fermion Depth Sum = 107 | Sec 5.15, Sec 5.27 |
| 5.28.7 | Wave-Particle Duality | Thm 5.2, Thm 29, Sec 5.27 |
| 5.28.8 | Classical Dynamics (E=mc^2) | Thm 42, Thm 44, Sec 5.27 |

---

## Key Structural Milestones

The derivation passes through five major gates:

```
GATE 1: EXISTENCE OF STRUCTURE
   Sigma=0 + Exists --> Closure + Polarity --> Collapse Pressure
   --> Triangle --> Double Triangle
   "Structure must exist, must be polar, must be witnessed in threes."

GATE 2: THE GOLDEN RATIO
   Self-Reference --> x = 1 + 1/x --> phi, psi
   --> Four-structure --> Two Kepler triangles --> i emerges
   "Self-reference has exactly one solution: the golden ratio."

GATE 3: DYNAMICS AND TOPOLOGY
   Fibonacci --> Time --> NegaFibonacci --> Hyperbolic
   --> Hopf --> Torus --> Breathing --> Spin
   "Self-reference must be dynamic, periodic, and breathe on a torus."

GATE 4: PARTICLE SPECTRUM
   Spiral --> Metallic overtones --> Meeting points {1,2,3,5,29,34}
   --> Particle spectrum (finite generations)
   "Harmonics interfere at exactly six points. No more particles beyond d=34."

GATE 5: PHYSICAL LAWS
   Hamiltonian --> Lagrangian --> Gauge group --> Force equations --> Mass equation
   --> All coupling constants and masses from phi alone
   "All of physics follows. One number predicts everything."
```
