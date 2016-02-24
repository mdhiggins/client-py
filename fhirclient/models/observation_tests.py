#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-02-24.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import observation
from .fhirdate import FHIRDate


class ObservationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Observation", js["resourceType"])
        return observation.Observation(js)
    
    def testObservation1(self):
        inst = self.instantiate_from("obs-genetics-example1-somatic.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation1(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation1(inst2)
    
    def implObservation1(self, inst):
        self.assertEqual(inst.code.coding[0].code, "55233-1")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.comments, "The EGFR p.L858R mutation has been associated with response to anti-EGFR therapy")
        self.assertEqual(inst.contained[0].id, "c1")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/geneticsGenomeBuild")
        self.assertEqual(inst.extension[0].valueString, "GRCh 37")
        self.assertEqual(inst.extension[1].url, "http://hl7.org/fhir/StructureDefinition/geneticsChromosome")
        self.assertEqual(inst.extension[1].valueCodeableConcept.coding[0].code, "NC_000007")
        self.assertEqual(inst.extension[1].valueCodeableConcept.coding[0].system, "http://www.ncbi.nlm.nih.gov/gene")
        self.assertEqual(inst.extension[1].valueCodeableConcept.text, "Homo sapiens chromosome 7")
        self.assertEqual(inst.extension[2].url, "http://hl7.org/fhir/StructureDefinition/geneticsGenomicStart")
        self.assertEqual(inst.extension[2].valueInteger, 55259515)
        self.assertEqual(inst.extension[3].url, "http://hl7.org/fhir/StructureDefinition/geneticsGenomicStop")
        self.assertEqual(inst.extension[3].valueInteger, 55259516)
        self.assertEqual(inst.extension[4].url, "http://hl7.org/fhir/StructureDefinition/geneticsSpecies")
        self.assertEqual(inst.extension[4].valueCodeableConcept.coding[0].code, "337915000")
        self.assertEqual(inst.extension[4].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.extension[4].valueCodeableConcept.text, "Homo sapiens")
        self.assertEqual(inst.extension[5].url, "http://hl7.org/fhir/StructureDefinition/geneticsCIGAR")
        self.assertEqual(inst.extension[5].valueString, "1M")
        self.assertEqual(inst.extension[6].url, "http://hl7.org/fhir/StructureDefinition/geneticsAssessedCondition")
        self.assertEqual(inst.extension[7].url, "http://hl7.org/fhir/StructureDefinition/geneticsReferenceAllele")
        self.assertEqual(inst.extension[7].valueString, "T")
        self.assertEqual(inst.extension[8].url, "http://hl7.org/fhir/StructureDefinition/geneticsObservedAllele")
        self.assertEqual(inst.extension[8].valueString, "G")
        self.assertEqual(inst.extension[9].url, "http://hl7.org/fhir/StructureDefinition/geneticsGene")
        self.assertEqual(inst.extension[9].valueCodeableConcept.coding[0].code, "3236")
        self.assertEqual(inst.extension[9].valueCodeableConcept.coding[0].display, "EGFR")
        self.assertEqual(inst.extension[9].valueCodeableConcept.coding[0].system, "http://www.genenames.org")
        self.assertEqual(inst.id, "genetics-example1-somatic")
        self.assertEqual(inst.interpretation.coding[0].code, "POS")
        self.assertEqual(inst.interpretation.coding[0].system, "http://hl7.org/fhir/v2/0078")
        self.assertEqual(inst.interpretation.text, "positive")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testObservation2(self):
        inst = self.instantiate_from("obs-genetics-example2-germline.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation2(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation2(inst2)
    
    def implObservation2(self, inst):
        self.assertEqual(inst.code.coding[0].code, "21636-6")
        self.assertEqual(inst.code.coding[0].display, "BRCA1 gene mutation analysis")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/geneticsGenomeBuild")
        self.assertEqual(inst.extension[0].valueString, "GRCh 37")
        self.assertEqual(inst.extension[1].url, "http://hl7.org/fhir/StructureDefinition/geneticsChromosome")
        self.assertEqual(inst.extension[1].valueCodeableConcept.coding[0].code, "NC_000017")
        self.assertEqual(inst.extension[1].valueCodeableConcept.coding[0].system, "http://www.ncbi.nlm.nih.gov/gene")
        self.assertEqual(inst.extension[1].valueCodeableConcept.text, "Homo sapiens chromosome 17")
        self.assertEqual(inst.extension[2].url, "http://hl7.org/fhir/StructureDefinition/geneticsGenomicStart")
        self.assertEqual(inst.extension[2].valueInteger, 41258504)
        self.assertEqual(inst.extension[3].url, "http://hl7.org/fhir/StructureDefinition/geneticsGenomicStop")
        self.assertEqual(inst.extension[3].valueInteger, 41258505)
        self.assertEqual(inst.extension[4].url, "http://hl7.org/fhir/StructureDefinition/geneticsReferenceAllele")
        self.assertEqual(inst.extension[4].valueString, "A")
        self.assertEqual(inst.extension[5].url, "http://hl7.org/fhir/StructureDefinition/geneticsObservedAllele")
        self.assertEqual(inst.extension[5].valueString, "C")
        self.assertEqual(inst.extension[6].url, "http://hl7.org/fhir/StructureDefinition/geneticsGene")
        self.assertEqual(inst.extension[6].valueCodeableConcept.coding[0].code, "1100")
        self.assertEqual(inst.extension[6].valueCodeableConcept.coding[0].display, "BRCA1")
        self.assertEqual(inst.extension[6].valueCodeableConcept.coding[0].system, "http://www.genenames.org")
        self.assertEqual(inst.extension[7].url, "http://hl7.org/fhir/StructureDefinition/geneticsDNASequenceVariation")
        self.assertEqual(inst.extension[7].valueString, "c.181T>G")
        self.assertEqual(inst.extension[8].url, "http://hl7.org/fhir/StructureDefinition/geneticsVariationId")
        self.assertEqual(inst.extension[8].valueCodeableConcept.coding[0].code, "17661")
        self.assertEqual(inst.extension[8].valueCodeableConcept.coding[0].display, "c.181T>G")
        self.assertEqual(inst.extension[8].valueCodeableConcept.coding[0].system, "http://www.ncbi.nlm.nih.gov/clinvar")
        self.assertEqual(inst.extension[9].url, "http://hl7.org/fhir/StructureDefinition/geneticsDNARegionName")
        self.assertEqual(inst.extension[9].valueString, "Exon 4")
        self.assertEqual(inst.id, "genetics-example2-germline")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testObservation3(self):
        inst = self.instantiate_from("obs-genetics-example3-mutationlist-1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation3(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation3(inst2)
    
    def implObservation3(self, inst):
        self.assertEqual(inst.code.coding[0].code, "49874-1")
        self.assertEqual(inst.code.coding[0].display, "ABCB4 gene mutation analysis")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[0].code.coding[0].code, "53037-8")
        self.assertEqual(inst.component[0].code.coding[0].display, "Genetic disease sequence variation interpretation")
        self.assertEqual(inst.component[0].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[0].valueCodeableConcept.coding[0].code, "LA6682-4")
        self.assertEqual(inst.component[0].valueCodeableConcept.coding[0].display, "Unknown significance")
        self.assertEqual(inst.component[0].valueCodeableConcept.coding[0].system, "http://www.genenames.org")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/geneticsDNASequenceVariation")
        self.assertEqual(inst.extension[0].valueString, "c.2708T>C")
        self.assertEqual(inst.extension[1].url, "http://hl7.org/fhir/StructureDefinition/geneticsDNARegionName")
        self.assertEqual(inst.extension[1].valueString, "Exon 23")
        self.assertEqual(inst.extension[2].url, "http://hl7.org/fhir/StructureDefinition/geneticsAminoAcidChange")
        self.assertEqual(inst.extension[2].valueString, "p.R969H")
        self.assertEqual(inst.id, "genetics-example3-mutationlist-1")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testObservation4(self):
        inst = self.instantiate_from("obs-genetics-example3-mutationlist-2.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation4(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation4(inst2)
    
    def implObservation4(self, inst):
        self.assertEqual(inst.code.coding[0].code, "49874-1")
        self.assertEqual(inst.code.coding[0].display, "ABCB4 gene mutation analysis")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[0].code.coding[0].code, "53037-8")
        self.assertEqual(inst.component[0].code.coding[0].display, "Genetic disease sequence variation interpretation")
        self.assertEqual(inst.component[0].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[0].valueCodeableConcept.coding[0].code, "LA6675-8")
        self.assertEqual(inst.component[0].valueCodeableConcept.coding[0].display, "Benign")
        self.assertEqual(inst.component[0].valueCodeableConcept.coding[0].system, "http://www.genenames.org")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/geneticsDNARegionName")
        self.assertEqual(inst.extension[0].valueString, "Exon 6")
        self.assertEqual(inst.extension[1].url, "http://hl7.org/fhir/StructureDefinition/geneticsAminoAcidChange")
        self.assertEqual(inst.extension[1].valueString, "p.N168N")
        self.assertEqual(inst.extension[2].url, "http://hl7.org/fhir/StructureDefinition/geneticsVariationId")
        self.assertEqual(inst.extension[2].valueCodeableConcept.coding[0].code, "1202283")
        self.assertEqual(inst.extension[2].valueCodeableConcept.coding[0].display, "c.181T>G")
        self.assertEqual(inst.extension[2].valueCodeableConcept.coding[0].system, "http://www.ncbi.nlm.nih.gov/projects/SNP")
        self.assertEqual(inst.id, "genetics-example3-mutationlist-2")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testObservation5(self):
        inst = self.instantiate_from("obs-genetics-example3-mutationlist-3.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation5(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation5(inst2)
    
    def implObservation5(self, inst):
        self.assertEqual(inst.code.coding[0].code, "49874-1")
        self.assertEqual(inst.code.coding[0].display, "ABCB4 gene mutation analysis")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[0].code.coding[0].code, "53037-8")
        self.assertEqual(inst.component[0].code.coding[0].display, "Genetic disease sequence variation interpretation")
        self.assertEqual(inst.component[0].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[0].valueCodeableConcept.coding[0].code, "LA6675-8")
        self.assertEqual(inst.component[0].valueCodeableConcept.coding[0].display, "Benign")
        self.assertEqual(inst.component[0].valueCodeableConcept.coding[0].system, "http://www.genenames.org")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/geneticsDNARegionName")
        self.assertEqual(inst.extension[0].valueString, "intron 16")
        self.assertEqual(inst.extension[1].url, "http://hl7.org/fhir/StructureDefinition/geneticsVariationId")
        self.assertEqual(inst.extension[1].valueCodeableConcept.coding[0].code, "31668")
        self.assertEqual(inst.extension[1].valueCodeableConcept.coding[0].display, "c.2211+16C>T")
        self.assertEqual(inst.extension[1].valueCodeableConcept.coding[0].system, "http://www.ncbi.nlm.nih.gov/projects/SNP")
        self.assertEqual(inst.id, "genetics-example3-mutationlist-3")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testObservation6(self):
        inst = self.instantiate_from("obs-genetics-example3-mutationlist-4.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation6(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation6(inst2)
    
    def implObservation6(self, inst):
        self.assertEqual(inst.code.coding[0].code, "49874-1")
        self.assertEqual(inst.code.coding[0].display, "ABCB4 gene mutation analysis")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[0].code.coding[0].code, "53037-8")
        self.assertEqual(inst.component[0].code.coding[0].display, "Genetic disease sequence variation interpretation")
        self.assertEqual(inst.component[0].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[0].valueCodeableConcept.coding[0].code, "LA6675-8")
        self.assertEqual(inst.component[0].valueCodeableConcept.coding[0].display, "Benign")
        self.assertEqual(inst.component[0].valueCodeableConcept.coding[0].system, "http://www.genenames.org")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/geneticsDNARegionName")
        self.assertEqual(inst.extension[0].valueString, "intron 26")
        self.assertEqual(inst.extension[1].url, "http://hl7.org/fhir/StructureDefinition/geneticsVariationId")
        self.assertEqual(inst.extension[1].valueCodeableConcept.coding[0].code, "31653")
        self.assertEqual(inst.extension[1].valueCodeableConcept.coding[0].display, "c.3487-16T>C")
        self.assertEqual(inst.extension[1].valueCodeableConcept.coding[0].system, "http://www.ncbi.nlm.nih.gov/projects/SNP")
        self.assertEqual(inst.id, "genetics-example3-mutationlist-4")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testObservation7(self):
        inst = self.instantiate_from("obs-genetics-example3-mutationlist.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation7(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation7(inst2)
    
    def implObservation7(self, inst):
        self.assertEqual(inst.code.coding[0].code, "49874-1")
        self.assertEqual(inst.code.coding[0].display, "ABCB4 gene mutation analysis")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/geneticsGenomeBuild")
        self.assertEqual(inst.extension[0].valueString, "GRCh 37")
        self.assertEqual(inst.extension[1].url, "http://hl7.org/fhir/StructureDefinition/geneticsGene")
        self.assertEqual(inst.extension[1].valueCodeableConcept.coding[0].code, "5244")
        self.assertEqual(inst.extension[1].valueCodeableConcept.coding[0].display, "ABCB4")
        self.assertEqual(inst.extension[1].valueCodeableConcept.coding[0].system, "http://www.genenames.org")
        self.assertEqual(inst.extension[2].url, "http://hl7.org/fhir/StructureDefinition/geneticsSpecies")
        self.assertEqual(inst.extension[2].valueCodeableConcept.coding[0].code, "337915000")
        self.assertEqual(inst.extension[2].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.extension[2].valueCodeableConcept.text, "Homo sapiens")
        self.assertEqual(inst.extension[3].url, "http://hl7.org/fhir/StructureDefinition/geneticsResult")
        self.assertEqual(inst.extension[4].url, "http://hl7.org/fhir/StructureDefinition/geneticsResult")
        self.assertEqual(inst.extension[5].url, "http://hl7.org/fhir/StructureDefinition/geneticsResult")
        self.assertEqual(inst.extension[6].url, "http://hl7.org/fhir/StructureDefinition/geneticsResult")
        self.assertEqual(inst.id, "genetics-example3-mutationlist")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testObservation8(self):
        inst = self.instantiate_from("observation-example-bloodpressure-cancel.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation8(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation8(inst2)
    
    def implObservation8(self, inst):
        self.assertEqual(inst.bodySite.coding[0].code, "368209003")
        self.assertEqual(inst.bodySite.coding[0].display, "Right arm")
        self.assertEqual(inst.bodySite.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.coding[0].code, "55284-4")
        self.assertEqual(inst.code.coding[0].display, "Blood pressure systolic & diastolic")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.comments, "In this example, the blood pressure measurements are not available due to cancellation of the order.  Data absent reason is present for each component")
        self.assertEqual(inst.component[0].code.coding[0].code, "8480-6")
        self.assertEqual(inst.component[0].code.coding[0].display, "Systolic blood pressure")
        self.assertEqual(inst.component[0].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[0].code.coding[1].code, "271649006")
        self.assertEqual(inst.component[0].code.coding[1].display, "Systolic blood pressure")
        self.assertEqual(inst.component[0].code.coding[1].system, "http://snomed.info/sct")
        self.assertEqual(inst.component[0].code.coding[2].code, "bp-s")
        self.assertEqual(inst.component[0].code.coding[2].display, "Systolic Blood pressure")
        self.assertEqual(inst.component[0].code.coding[2].system, "http://acme.org/devices/clinical-codes")
        self.assertEqual(inst.component[0].dataAbsentReason.coding[0].code, "not-asked")
        self.assertEqual(inst.component[0].dataAbsentReason.coding[0].display, "Not Asked")
        self.assertEqual(inst.component[0].dataAbsentReason.coding[0].system, "http://hl7.org/fhir/data-absent-reason")
        self.assertEqual(inst.component[1].code.coding[0].code, "8462-4")
        self.assertEqual(inst.component[1].code.coding[0].display, "Diastolic blood pressure")
        self.assertEqual(inst.component[1].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[1].dataAbsentReason.coding[0].code, "not-asked")
        self.assertEqual(inst.component[1].dataAbsentReason.coding[0].display, "Not Asked")
        self.assertEqual(inst.component[1].dataAbsentReason.coding[0].system, "http://hl7.org/fhir/data-absent-reason")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2012-09-17").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2012-09-17")
        self.assertEqual(inst.id, "blood-pressure-cancel")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value, "urn:uuid:187e0c12-8dd2-67e2-99b2-bf273c878281")
        self.assertEqual(inst.interpretation.coding[0].code, "L")
        self.assertEqual(inst.interpretation.coding[0].display, "Below low normal")
        self.assertEqual(inst.interpretation.coding[0].system, "http://hl7.org/fhir/v2/0078")
        self.assertEqual(inst.interpretation.text, "low")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2014-01-30T22:35:23+11:00").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2014-01-30T22:35:23+11:00")
        self.assertEqual(inst.status, "cancelled")
        self.assertEqual(inst.text.status, "generated")
    
    def testObservation9(self):
        inst = self.instantiate_from("observation-example-bloodpressure.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation9(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation9(inst2)
    
    def implObservation9(self, inst):
        self.assertEqual(inst.bodySite.coding[0].code, "368209003")
        self.assertEqual(inst.bodySite.coding[0].display, "Right arm")
        self.assertEqual(inst.bodySite.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.coding[0].code, "55284-4")
        self.assertEqual(inst.code.coding[0].display, "Blood pressure systolic & diastolic")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[0].code.coding[0].code, "8480-6")
        self.assertEqual(inst.component[0].code.coding[0].display, "Systolic blood pressure")
        self.assertEqual(inst.component[0].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[0].code.coding[1].code, "271649006")
        self.assertEqual(inst.component[0].code.coding[1].display, "Systolic blood pressure")
        self.assertEqual(inst.component[0].code.coding[1].system, "http://snomed.info/sct")
        self.assertEqual(inst.component[0].code.coding[2].code, "bp-s")
        self.assertEqual(inst.component[0].code.coding[2].display, "Systolic Blood pressure")
        self.assertEqual(inst.component[0].code.coding[2].system, "http://acme.org/devices/clinical-codes")
        self.assertEqual(inst.component[0].valueQuantity.unit, "mm[Hg]")
        self.assertEqual(inst.component[0].valueQuantity.value, 107)
        self.assertEqual(inst.component[1].code.coding[0].code, "8462-4")
        self.assertEqual(inst.component[1].code.coding[0].display, "Diastolic blood pressure")
        self.assertEqual(inst.component[1].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[1].valueQuantity.unit, "mm[Hg]")
        self.assertEqual(inst.component[1].valueQuantity.value, 60)
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2012-09-17").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2012-09-17")
        self.assertEqual(inst.id, "blood-pressure")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value, "urn:uuid:187e0c12-8dd2-67e2-99b2-bf273c878281")
        self.assertEqual(inst.interpretation.coding[0].code, "L")
        self.assertEqual(inst.interpretation.coding[0].display, "Below low normal")
        self.assertEqual(inst.interpretation.coding[0].system, "http://hl7.org/fhir/v2/0078")
        self.assertEqual(inst.interpretation.text, "low")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2014-01-30T22:35:23+11:00").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2014-01-30T22:35:23+11:00")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testObservation10(self):
        inst = self.instantiate_from("observation-example-f001-glucose.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation10(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation10(inst2)
    
    def implObservation10(self, inst):
        self.assertEqual(inst.code.coding[0].code, "15074-8")
        self.assertEqual(inst.code.coding[0].display, "Glucose [Moles/volume] in Blood")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.effectivePeriod.end.date, FHIRDate("2013-04-05T09:30:10+01:00").date)
        self.assertEqual(inst.effectivePeriod.end.as_json(), "2013-04-05T09:30:10+01:00")
        self.assertEqual(inst.effectivePeriod.start.date, FHIRDate("2013-04-02T09:30:10+01:00").date)
        self.assertEqual(inst.effectivePeriod.start.as_json(), "2013-04-02T09:30:10+01:00")
        self.assertEqual(inst.id, "f001")
        self.assertEqual(inst.identifier[0].system, "http://www.bmc.nl/zorgportal/identifiers/observations")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "6323")
        self.assertEqual(inst.interpretation.coding[0].code, "H")
        self.assertEqual(inst.interpretation.coding[0].display, "Above high normal")
        self.assertEqual(inst.interpretation.coding[0].system, "http://hl7.org/fhir/v2/0078")
        self.assertEqual(inst.issued.date, FHIRDate("2013-04-03T15:30:10+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-04-03T15:30:10+01:00")
        self.assertEqual(inst.referenceRange[0].high.code, "mmol/L")
        self.assertEqual(inst.referenceRange[0].high.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.referenceRange[0].high.unit, "mmol/l")
        self.assertEqual(inst.referenceRange[0].high.value, 6.2)
        self.assertEqual(inst.referenceRange[0].low.code, "mmol/L")
        self.assertEqual(inst.referenceRange[0].low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.referenceRange[0].low.unit, "mmol/l")
        self.assertEqual(inst.referenceRange[0].low.value, 3.1)
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueQuantity.code, "mmol/L")
        self.assertEqual(inst.valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.valueQuantity.unit, "mmol/l")
        self.assertEqual(inst.valueQuantity.value, 6.3)

