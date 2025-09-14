
// 15 sample properties.


window.PROPERTIES = [
 
  {
    id: "001",
    address: "12 Wattle Street, Albury",
    zone: "R1",
    lotSize_m2: 700,
    bushfireProne: false,
    heritageListed: false,
    cornerLot: false,
    floodAffected: false,
    slopeRise_m: 0.5,
    proposal: {
      type: "shed",
      width_m: 3, length_m: 4, height_m: 2.4,
      attachedToDwelling: false,
      location: "rear",
      setbackFront_m: 7, setbackSide_m: 0.9, setbackRear_m: 1.0
    }
  },
  {
    id: "002",
    address: "5 Rivergum Ct, Thurgoona",
    zone: "R2",
    lotSize_m2: 1200,
    bushfireProne: true,
    heritageListed: false,
    cornerLot: false,
    floodAffected: false,
    slopeRise_m: 0.3,
    proposal: {
      type: "verandah", // “Patio 4x5m attached to rear” ≈ verandah/pergola
      width_m: 4, length_m: 5, height_m: 2.7,
      attachedToDwelling: true,
      location: "rear",
      setbackFront_m: 8, setbackSide_m: 0.9, setbackRear_m: 1.5
    }
  },
];