
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
  {
    id: "003",
    address: "88 Olive Street, Central Albury",
    zone: "B4",
    lotSize_m2: 480,
    bushfireProne: false,
    heritageListed: true,
    cornerLot: false,
    floodAffected: false,
    slopeRise_m: 0.2,
    proposal: {
      type: "shed", // “near fence”
      width_m: 2, length_m: 3, height_m: 2.4,
      attachedToDwelling: false,
      location: "side",
      setbackFront_m: 6, setbackSide_m: 0.6, setbackRear_m: 1.0
    }
  },
  {
    id: "004",
    address: "34 Mahogany Drive, Glenroy",
    zone: "R5",
    lotSize_m2: 1800,
    bushfireProne: true,
    heritageListed: false,
    cornerLot: false,
    floodAffected: false,
    slopeRise_m: 0.8,
    proposal: {
      type: "verandah", // “Detached patio 6x4”
      width_m: 6, length_m: 4, height_m: 2.7,
      attachedToDwelling: false,
      location: "rear",
      setbackFront_m: 9, setbackSide_m: 1.2, setbackRear_m: 2.0
    }
  },
  {
    id: "005",
    address: "22 Clyne Ave, East Albury",
    zone: "R1",
    lotSize_m2: 850,
    bushfireProne: false,
    heritageListed: false,
    cornerLot: false,
    floodAffected: false,
    slopeRise_m: 0.4,
    proposal: {
      type: "verandah", // “Pergola 3x4m attached”
      width_m: 3, length_m: 4, height_m: 2.6,
      attachedToDwelling: true,
      location: "rear",
      setbackFront_m: 7, setbackSide_m: 0.9, setbackRear_m: 1.2
    }
  },
];