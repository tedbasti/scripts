REM  *****  BASIC  *****

Function getinteger(optional value as Variant)
	if isNumeric(value) Then
		getinteger = value
	else 
		getinteger = 0
	End if
End Function

Function mysum(values as Variant)
	Dim result as Integer
	Dim temp as Variant
	result = 0
	if (isArray(values)) Then
		Dim i as Integer
		Dim lvalue as Variant
		Dim size as Integer
		For i = LBound(values,1) to UBound(values,1)
			temp = LBound(values,2)
			size = UBound(values,2) - temp + 1
			lvalue = values(i,temp)
			if (size > 1) Then
				Rem if a x is on the left, use the whole value of the right
				if (strcomp(lvalue,"x") = 0) Then
					result = result + getinteger(values(i,temp+1))
				elseif isNumeric(lvalue) Then
					result = result + lvalue
				End if
			else
				result = result + getinteger(lvalue)
			End if
		Next
	else
		result = getinteger(values)
	End if
	mysum = result
End Function