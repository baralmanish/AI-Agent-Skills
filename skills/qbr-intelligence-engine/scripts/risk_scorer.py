"""
Risk Scorer: Identifies and scores business risks for QBR
Uses standardized framework to rate and prioritize risks
"""

class RiskScorer:
    """Score and prioritize business risks"""
    
    RISK_CATEGORIES = {
        'customer_concentration': {
            'description': 'Revenue dependent on too few customers',
            'indicators': ['top_customer_percent_revenue', 'customer_concentration_herfindahl']
        },
        'retention': {
            'description': 'High churn or declining retention metrics',
            'indicators': ['churn_rate', 'nrr_trend', 'customer_satisfaction']
        },
        'market': {
            'description': 'Market competition or demand decline',
            'indicators': ['competitive_pressure', 'addressable_market_trend', 'win_rate']
        },
        'execution': {
            'description': 'Inability to execute on plans',
            'indicators': ['okr_completion', 'headcount_plan_vs_actual', 'product_velocity']
        },
        'financing': {
            'description': 'Insufficient capital to reach next milestone',
            'indicators': ['runway_months', 'burn_rate_trend', 'revenue_growth_rate']
        },
        'talent': {
            'description': 'Key talent loss or inability to hire',
            'indicators': ['turnover_rate', 'open_headcount_percent', 'engineering_retention']
        },
        'product_market_fit': {
            'description': 'Declining product adoption or engagement',
            'indicators': ['dau_trend', 'feature_adoption', 'nps_score']
        }
    }
    
    @staticmethod
    def score_risk(risk_name, **indicators):
        """
        Score a specific risk on a scale of 1-10
        Args:
            risk_name: Name of risk from RISK_CATEGORIES
            **indicators: Relevant metrics for scoring
        Returns:
            Risk score, severity level, and recommendations
        """
        if risk_name not in RiskScorer.RISK_CATEGORIES:
            return None
        
        scores = []
        
        # Score based on specific indicators
        if 'top_customer_percent_revenue' in indicators:
            pct = indicators['top_customer_percent_revenue']
            if pct > 40:
                scores.append(9)
            elif pct > 25:
                scores.append(7)
            elif pct > 15:
                scores.append(5)
            else:
                scores.append(2)
        
        if 'churn_rate' in indicators:
            churn = indicators['churn_rate']
            if churn > 5:  # 5% monthly
                scores.append(9)
            elif churn > 3:
                scores.append(7)
            elif churn > 1.5:
                scores.append(5)
            else:
                scores.append(2)
        
        if 'nrr_trend' in indicators:
            trend = indicators['nrr_trend']  # 'improving', 'stable', 'declining'
            if trend == 'declining':
                scores.append(8)
            elif trend == 'stable':
                scores.append(4)
            else:
                scores.append(2)
        
        if 'runway_months' in indicators:
            runway = indicators['runway_months']
            if runway < 6:
                scores.append(10)
            elif runway < 12:
                scores.append(8)
            elif runway < 18:
                scores.append(6)
            else:
                scores.append(2)
        
        if 'burn_rate_trend' in indicators:
            trend = indicators['burn_rate_trend']  # 'accelerating', 'stable', 'improving'
            if trend == 'accelerating':
                scores.append(8)
            elif trend == 'stable':
                scores.append(5)
            else:
                scores.append(2)
        
        if 'okr_completion' in indicators:
            completion = indicators['okr_completion']  # percentage
            if completion < 50:
                scores.append(9)
            elif completion < 70:
                scores.append(7)
            elif completion < 85:
                scores.append(5)
            else:
                scores.append(2)
        
        if not scores:
            avg_score = 5  # Default neutral score
        else:
            avg_score = sum(scores) / len(scores)
        
        severity = RiskScorer.classify_severity(avg_score)
        
        return {
            'risk': risk_name,
            'score': round(avg_score, 1),
            'severity': severity,
            'indicators_evaluated': len(scores)
        }
    
    @staticmethod
    def classify_severity(score):
        """Classify risk severity based on score"""
        if score >= 8:
            return 'critical'
        elif score >= 6:
            return 'high'
        elif score >= 4:
            return 'medium'
        else:
            return 'low'
    
    @staticmethod
    def create_risk_matrix(risks):
        """
        Create a probability × impact risk matrix
        Args:
            risks: List of risk dicts with score and description
        Returns:
            Organized risk matrix
        """
        # Assume score translates to both probability and impact
        matrix = {
            'critical': [],
            'high': [],
            'medium': [],
            'low': []
        }
        
        for risk in risks:
            severity = risk.get('severity', 'medium')
            matrix[severity].append(risk)
        
        return matrix


class RiskMitigationPlanner:
    """Plan mitigation strategies for identified risks"""
    
    MITIGATION_PLAYBOOKS = {
        'customer_concentration': {
            'tactics': [
                'Accelerate new customer acquisition (target 3+ new enterprise customers)',
                'Build industry partnerships to diversify revenue streams',
                'Implement dedicated account management for top customers',
                'Develop product features for adjacent use cases to increase stickiness'
            ],
            'leading_indicators': ['new_customer_adds', 'revenue_per_customer_trend', 'customer_nps'],
            'timeline_weeks': 8
        },
        'retention': {
            'tactics': [
                'Launch customer success program (proactive outreach to at-risk accounts)',
                'Implement usage-based alerting to catch churn signals early',
                'Create feature adoption program targeting key features',
                'Conduct win/loss analysis with churned customers'
            ],
            'leading_indicators': ['monthly_churn_rate', 'nrr', 'customer_satisfaction'],
            'timeline_weeks': 6
        },
        'financing': {
            'tactics': [
                'Begin fundraising conversations with existing investors',
                'Model multiple paths to profitability',
                'Implement cost control measures (hiring freeze, OpEx audit)',
                'Explore strategic partnerships or revenue deals'
            ],
            'leading_indicators': ['runway_months', 'cash_position', 'burn_rate'],
            'timeline_weeks': 12
        },
        'execution': {
            'tactics': [
                'Simplify OKRs to top 3 priorities (vs. 10+)',
                'Increase planning cadence (weekly vs. monthly check-ins)',
                'Add accountability (individual DRIs with public commitments)',
                'Remove blockers through weekly exec sync'
            ],
            'leading_indicators': ['okr_completion', 'sprint_velocity', 'milestone_hit_rate'],
            'timeline_weeks': 4
        }
    }
    
    @staticmethod
    def get_mitigation_plan(risk_name):
        """Get recommended mitigation strategy for a risk"""
        if risk_name not in RiskMitigationPlanner.MITIGATION_PLAYBOOKS:
            return None
        
        playbook = RiskMitigationPlanner.MITIGATION_PLAYBOOKS[risk_name]
        return {
            'risk': risk_name,
            'tactics': playbook['tactics'],
            'leading_indicators': playbook['leading_indicators'],
            'estimated_timeline_weeks': playbook['timeline_weeks'],
            'escalation_trigger': f"If {playbook['leading_indicators'][0]} worsens by >10% in next 2 weeks"
        }


if __name__ == "__main__":
    # Example usage
    scorer = RiskScorer()
    
    # Score customer concentration risk
    risk_score = scorer.score_risk(
        'customer_concentration',
        top_customer_percent_revenue=35
    )
    print(f"Customer Concentration Risk: {risk_score}")
    
    # Score retention risk
    retention_risk = scorer.score_risk(
        'retention',
        churn_rate=4.2,
        nrr_trend='declining'
    )
    print(f"Retention Risk: {retention_risk}")
    
    # Score financing risk
    financing_risk = scorer.score_risk(
        'financing',
        runway_months=8,
        burn_rate_trend='accelerating'
    )
    print(f"Financing Risk: {financing_risk}")
    
    # Get mitigation plan
    planner = RiskMitigationPlanner()
    mitigation = planner.get_mitigation_plan('customer_concentration')
    print(f"\nMitigation Plan: {mitigation}")
