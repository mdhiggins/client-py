#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Flag) on 2016-02-24.
#  2016, SMART Health IT.


from . import domainresource

class Flag(domainresource.DomainResource):
    """ Key information to flag to healthcare providers.
    
    Prospective warnings of potential issues when providing care to the
    patient.
    """
    
    resource_name = "Flag"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.author = None
        """ Flag creator.
        Type `FHIRReference` referencing `Device, Organization, Patient, Practitioner` (represented as `dict` in JSON). """
        
        self.category = None
        """ Clinical, administrative, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ Partially deaf, Requires easy open caps, No permanent address, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Alert relevant during encounter.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.period = None
        """ Time period when flag is active.
        Type `Period` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | inactive | entered-in-error.
        Type `str`. """
        
        self.subject = None
        """ Who/What is flag about?.
        Type `FHIRReference` referencing `Patient, Location, Group, Organization, Practitioner` (represented as `dict` in JSON). """
        
        super(Flag, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Flag, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False),
            ("category", "category", codeableconcept.CodeableConcept, False),
            ("code", "code", codeableconcept.CodeableConcept, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("period", "period", period.Period, False),
            ("status", "status", str, False),
            ("subject", "subject", fhirreference.FHIRReference, False),
        ])
        return js


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import period
