module calc_temp
    implicit none

    contains

    subroutine compute_profile(a_param, damping_param, pressure, nlayers, result)
        real(8), intent(in) :: a_param
        real(8), intent(in) :: damping_param
        real(8), intent(in) :: pressure(nlayers)
        integer, intent(in) :: nlayers
        real(8), intent(out) :: result(nlayers)

        result = a_param*exp(damping_param*log10(pressure))
    end subroutine
end module