# Copyright (c) 2022, Ajira Group and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SalesVATRegister(Document):
	def before_save(self):
		if self.s_taxable_amount == None or self.s_taxable_amount == 0:
			self.s_taxable_amount = None
		if self.s_total == None or self.s_total == 0:
			self.s_total = None


		if self.s_taxable_amount == None and self.s_total == None:
			frappe.throw("Amount cannot be zero !")

		elif self.s_taxable_amount != None and self.s_total == None:
			self.s_vat = self.s_taxable_amount * 0.13
			self.s_total = self.s_taxable_amount + self.s_vat

		elif self.s_taxable_amount == None and self.s_total != None:
			self.s_taxable_amount = self.s_total / 1.13
			self.s_vat = self.s_taxable_amount * 0.13

		elif self.s_taxable_amount != None and self.s_total != None:
			if (self.s_vat == self.s_taxable_amount * 0.13) and (self.s_total != self.s_taxable_amount + self.s_vat):
				self.s_taxable_amount = self.s_total / 1.13
				self.s_vat = self.s_taxable_amount * 0.13

			elif (self.s_vat != self.s_taxable_amount * 0.13):
				self.s_vat = self.s_taxable_amount * 0.13
				self.s_total = self.s_taxable_amount + self.s_vat

				
		


