module "executive_summary" {
  source = "./modules/executive_summary"
  customer_name = var.customer_name
  business_goals = var.business_goals
  current_issues = var.current_issues
  key_benefits_drivers = var.key_benefits_drivers
  rackspace_differentiation = var.rackspace_differentiation
}