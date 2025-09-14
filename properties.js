
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
  {
    id: "006",
    address: "17 Norwood Street, Lavington",
    zone: "R2",
    lotSize_m2: 600,
    bushfireProne: false,
    heritageListed: false,
    cornerLot: true,
    floodAffected: false,
    slopeRise_m: 0.3,
    proposal: {
      type: "shed",
      width_m: 3, length_m: 6, height_m: 2.7,
      attachedToDwelling: false,
      location: "side",
      setbackFront_m: 6, setbackSide_m: 1.0, setbackRear_m: 1.0
    }
  },
  {
    id: "007",
    address: "90 Ryan Rd, Splitters Creek",
    zone: "RU4",
    lotSize_m2: 10000,
    bushfireProne: true,
    heritageListed: false,
    cornerLot: false,
    floodAffected: false,
    slopeRise_m: 1.0,
    proposal: {
      type: "shed", // Shed 9x7m farm use
      width_m: 9, length_m: 7, height_m: 3.5,
      attachedToDwelling: false,
      location: "farm",
      setbackFront_m: 15, setbackSide_m: 5, setbackRear_m: 5
    }
  },
  {
    id: "008",
    address: "76 Fallon Street, North Albury",
    zone: "R2",
    lotSize_m2: 520,
    bushfireProne: false,
    heritageListed: false,
    cornerLot: false,
    floodAffected: false,
    slopeRise_m: 0.2,
    proposal: {
      type: "carport", // Carport 3x5m front
      width_m: 3, length_m: 5, height_m: 2.6,
      attachedToDwelling: true,
      location: "front",
      setbackFront_m: 5.5, setbackSide_m: 0.9, setbackRear_m: 6
    }
  },
  {
    id: "009",
    address: "3 Boundary Rd, Table Top",
    zone: "RU1",
    lotSize_m2: 40000,
    bushfireProne: true,
    heritageListed: false,
    cornerLot: false,
    floodAffected: false,
    slopeRise_m: 2.0,
    proposal: {
      type: "shed", // Detached shed 12x6m
      width_m: 12, length_m: 6, height_m: 4.0,
      attachedToDwelling: false,
      location: "rear",
      setbackFront_m: 20, setbackSide_m: 10, setbackRear_m: 10
    }
  },
];