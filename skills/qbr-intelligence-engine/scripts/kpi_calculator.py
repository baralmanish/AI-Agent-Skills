"""
KPI Calculator: Calculates growth rates, trends, and comparative metrics
Used by QBR Intelligence Engine for precise calculations
"""

class KPICalculator:
    """Calculate key performance indicators and business metrics"""
    
    @staticmethod
    def calculate_growth_rate(current, previous, annualize=False):
        """
        Calculate QoQ or YoY growth rate
        Args:
            current: Current period value
            previous: Previous period value
            annualize: If True, annualizes QoQ rate to YoY equivalent
        Returns:
            Growth rate as percentage
        """
        if previous == 0:
            return None
        growth = ((current - previous) / abs(previous)) * 100
        if annualize:
            growth = ((1 + growth/100) ** 4 - 1) * 100
        return round(growth, 2)
    
    @staticmethod
    def calculate_mrr_arr(monthly_recurring_revenue=None, annual_recurring_revenue=None):
        """Convert between MRR and ARR"""
        if monthly_recurring_revenue:
            return monthly_recurring_revenue * 12
        elif annual_recurring_revenue:
            return annual_recurring_revenue / 12
        return None
    
    @staticmethod
    def calculate_unit_economics(cac, ltv):
        """Calculate LTV:CAC ratio and payback period"""
        if cac == 0:
            return None
        ratio = ltv / cac
        # Assumes average customer lifetime = 12 months, average payment = LTV/12
        payback_months = (cac / (ltv / 12)) if ltv > 0 else None
        return {
            'ltv_cac_ratio': round(ratio, 2),
            'payback_months': round(payback_months, 1) if payback_months else None,
            'health': 'excellent' if ratio >= 3 else 'good' if ratio >= 2 else 'concerning'
        }
    
    @staticmethod
    def calculate_nrr_trajectory(cohort_revenues, cohort_ages):
        """
        Calculate Net Revenue Retention trend
        Args:
            cohort_revenues: List of revenues by cohort (newest first)
            cohort_ages: List of ages in months for each cohort
        Returns:
            NRR trend analysis
        """
        if len(cohort_revenues) < 2:
            return None
        
        # Calculate NRR for each cohort if data available
        nrr_trend = []
        for i, revenue in enumerate(cohort_revenues[:-1]):
            next_revenue = cohort_revenues[i + 1]
            nrr = (next_revenue / revenue) * 100 if revenue > 0 else None
            nrr_trend.append({'age_months': cohort_ages[i], 'nrr': nrr})
        
        return {
            'nrr_by_cohort': nrr_trend,
            'trend': 'improving' if nrr_trend[-1]['nrr'] > nrr_trend[0]['nrr'] else 'declining'
        }
    
    @staticmethod
    def calculate_burn_rate(cash_spent, runway_months=None):
        """Calculate monthly burn rate and runway"""
        monthly_burn = cash_spent / 3 if cash_spent else 0  # Assuming quarterly data
        return {
            'monthly_burn': round(monthly_burn, 0),
            'quarterly_burn': round(cash_spent, 0),
            'runway_months': runway_months
        }
    
    @staticmethod
    def calculate_margin(revenue, cost):
        """Calculate margin as percentage"""
        if revenue == 0:
            return 0
        return round(((revenue - cost) / revenue) * 100, 2)
    
    @staticmethod
    def classify_trend(current, previous):
        """Classify metric trend"""
        if previous == 0:
            return "new"
        growth = ((current - previous) / abs(previous)) * 100
        if growth > 10:
            return "accelerating"
        elif growth > 0:
            return "growing"
        elif growth > -10:
            return "declining"
        else:
            return "deteriorating"


class BenchmarkComparator:
    """Compare company metrics against industry benchmarks"""
    
    BENCHMARKS = {
        'SaaS_Growth': {
            'magic_number': {'excellent': 0.75, 'good': 0.5, 'warning': 0.3},
            'nrr': {'excellent': 120, 'good': 110, 'warning': 100},
            'cac_payback': {'excellent': 12, 'good': 18, 'warning': 24},
            'rule_of_40': {'excellent': 40, 'good': 30, 'warning': 20}
        },
        'SaaS_Mature': {
            'magic_number': {'excellent': 0.4, 'good': 0.25, 'warning': 0.15},
            'nrr': {'excellent': 110, 'good': 105, 'warning': 100},
            'cac_payback': {'excellent': 18, 'good': 24, 'warning': 36}
        },
        'Marketplace': {
            'take_rate': {'excellent': 0.30, 'good': 0.20, 'warning': 0.10},
            'gvr_ratio': {'excellent': 3.0, 'good': 2.0, 'warning': 1.0}
        }
    }
    
    @staticmethod
    def compare_metric(metric_name, company_value, company_stage):
        """Compare company metric to benchmark"""
        benchmarks = BenchmarkComparator.BENCHMARKS.get(company_stage, {})
        metric_bench = benchmarks.get(metric_name, {})
        
        if not metric_bench:
            return {'status': 'no_benchmark'}
        
        if company_value >= metric_bench.get('excellent', 0):
            status = 'excellent'
        elif company_value >= metric_bench.get('good', 0):
            status = 'good'
        else:
            status = 'warning'
        
        return {
            'company_value': company_value,
            'status': status,
            'benchmarks': metric_bench
        }


if __name__ == "__main__":
    # Example usage
    calc = KPICalculator()
    
    # Growth calculation
    growth = calc.calculate_growth_rate(current=2500000, previous=2000000)
    print(f"QoQ Growth: {growth}%")
    
    # Unit economics
    unit_econ = calc.calculate_unit_economics(cac=500, ltv=3000)
    print(f"Unit Economics: {unit_econ}")
    
    # Burn rate
    burn = calc.calculate_burn_rate(cash_spent=750000, runway_months=18)
    print(f"Burn Analysis: {burn}")
